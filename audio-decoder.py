import pyaudio
import numpy as np
from scipy.fftpack import fft
from symbol_decoder import SymbolDecoder

SAMPLE_RATE = 44100
DURATION = 0.02
FREQ_SPACE = 1000
FREQ_MARK = 2000

FRAME_SIZE = 128
FRAME_PER_SYMBOL = int(SAMPLE_RATE * DURATION) / FRAME_SIZE

print("Sample per symbol: ", FRAME_PER_SYMBOL)


class FSKDetector:
    def __init__(self, sample_rate, frame_size, space_freq, mark_freq):
        frequencies = np.fft.fftfreq(frame_size, d=1 / sample_rate)
        self.space_freq_idx = np.where(
            (frequencies >= space_freq - 100) & (frequencies <= space_freq + 100)
        )[0]
        self.mark_freq_idx = np.where(
            (frequencies >= mark_freq - 100) & (frequencies <= mark_freq + 100)
        )[0]

    def detect(self, signal):
        fft_data = fft(signal)
        space_power = np.sum(np.abs(fft_data[self.space_freq_idx]) ** 2)
        mark_power = np.sum(np.abs(fft_data[self.mark_freq_idx]) ** 2)
        if space_power < 0.0001 and mark_power < 0.0001:
            return None

        if space_power > mark_power:
            return 0
        else:
            return 1


# PyAudio 설정
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=FRAME_SIZE,
)

detector = FSKDetector(SAMPLE_RATE, FRAME_SIZE, FREQ_SPACE, FREQ_MARK)
decoder = SymbolDecoder(FRAME_PER_SYMBOL, logging=False)

preamble = [0, 0, 0, 1, 0, 0, 0, 1] * 2
preamble_buffer = []
byte_buffer = []

while True:
    data = stream.read(FRAME_SIZE)
    data = np.frombuffer(data, dtype=np.float32)

    bit = detector.detect(data)
    bit = decoder.process(bit)

    if bit is not None:
        byte_buffer.append(bit)
        if len(byte_buffer) == 8:
            byte = 0
            for i in range(8):
                byte |= byte_buffer[i] << i
            print(chr(byte), end="", flush=True)
            byte_buffer = []

        preamble_buffer.append(bit)
        if len(preamble_buffer) > len(preamble):
            preamble_buffer.pop(0)
        if preamble_buffer == preamble:
            byte_buffer = []
