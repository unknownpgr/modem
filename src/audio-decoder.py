import sys

import numpy as np
import pyaudio
from scipy import signal

from codec import Codec


class AudioSource:
    def __init__(self, sample_rate=44100):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=sample_rate,
            input=True,
            frames_per_buffer=1,
        )

    def read(self):
        data = self.stream.read(1)
        return np.frombuffer(data, dtype=np.float32)[0]

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


class FirFilter:
    def __init__(self, cutoff_freq, num_taps, sample_rate=44100, bandwidth=50):
        nyquist = sample_rate / 2
        low_cutoff = (cutoff_freq - bandwidth / 2) / nyquist
        high_cutoff = (cutoff_freq + bandwidth / 2) / nyquist
        self.fir_coefficients = signal.firwin(
            num_taps, [low_cutoff, high_cutoff], pass_zero=False
        )
        self.buffer = np.zeros(num_taps)

    def clear(self):
        self.buffer = np.zeros(len(self.buffer))

    def filter(self, audio):
        self.buffer[:-1] = self.buffer[1:]
        self.buffer[-1] = audio
        return np.dot(self.buffer, self.fir_coefficients)


class EnvelopeFilter:
    def __init__(self, samples=50):
        self.buffer = np.zeros(samples)

    def clear(self):
        self.buffer = np.zeros(len(self.buffer))

    def filter(self, audio):
        self.buffer[:-1] = self.buffer[1:]
        self.buffer[-1] = audio
        return np.mean(np.abs(self.buffer))


class IirFilter:
    def __init__(self, cutoff_freq, sample_rate=44100):
        self.const = 1 - 2 * np.pi * cutoff_freq / sample_rate
        self.iir = 0

    def clear(self):
        self.iir = 0

    def filter(self, audio):
        self.iir = self.const * self.iir + (1 - self.const) * abs(audio)
        return self.iir


class BitFilter:
    def __init__(self, baud_rate, shift_ratio=1 / 20, sample_rate=44100):
        self.baud_rate = baud_rate
        self.sample_rate = sample_rate

        self.arr = sample_rate / baud_rate  # Note that it might not be an integer
        self.shift = self.arr * shift_ratio
        self.counter = 0
        self.bit_counter = 0
        self.shift_counter = 0
        self.prev_bit = 0

    def clear(self):
        self.counter = 0
        self.shift_counter = 0

    def filter(self, bit):
        if bit != self.prev_bit:
            if self.counter < self.arr / 2:
                self.shift_counter += 1
            else:
                self.shift_counter -= 1
        self.prev_bit = bit

        # Increment the counter
        self.counter += 1
        self.bit_counter += bit

        # output_bit = self.bit_counter / self.arr
        output_bit = None
        if self.counter > self.arr:
            # Determine the output bit
            output_bit = int(self.bit_counter / self.arr > 0.5)
            # output_bit = self.counter / self.arr
            self.bit_counter = 0

            # Wrap the counter
            while self.counter > self.arr:
                self.counter -= self.arr

            # Shift the counter
            if self.shift_counter > 0:
                self.counter -= self.shift
            elif self.shift_counter < 0:
                self.counter += self.shift
            self.shift_counter = 0

        return output_bit


SAMPLE_RATE = 44100
BAUD_RATE = 1000

FREQ_SPACE = 6500
FREQ_MARK = 8000
FIR_SIZE = 45
FIR_BANDWIDTH = 50
ENVF_SAMPLES = 50
BITF_SHIFT_RATIO = 1 / 40

src = AudioSource()
iirf = IirFilter(cutoff_freq=1, sample_rate=SAMPLE_RATE)

fir_space = FirFilter(
    cutoff_freq=FREQ_SPACE,
    num_taps=FIR_SIZE,
    bandwidth=FIR_BANDWIDTH,
)
fir_mark = FirFilter(
    cutoff_freq=FREQ_MARK,
    num_taps=FIR_SIZE,
    bandwidth=FIR_BANDWIDTH,
)

envf_space = EnvelopeFilter(samples=ENVF_SAMPLES)
envf_mark = EnvelopeFilter(samples=ENVF_SAMPLES)

bitf = BitFilter(
    baud_rate=BAUD_RATE,
    shift_ratio=BITF_SHIFT_RATIO,
    sample_rate=SAMPLE_RATE,
)
codec = Codec()
mag = 0

try:
    while True:
        audio = src.read() / max(mag, 0.1)
        mag = iirf.filter(abs(audio))

        filter_mark = fir_mark.filter(audio)
        filter_space = fir_space.filter(audio)

        env_mark = envf_mark.filter(filter_mark)
        env_space = envf_space.filter(filter_space)

        bit = int(env_mark > env_space)
        output_bit = bitf.filter(bit)
        byte = codec.decode(output_bit)
        if byte != None:
            sys.stdout.buffer.write(byte)
            sys.stdout.buffer.flush()
except KeyboardInterrupt:
    pass
