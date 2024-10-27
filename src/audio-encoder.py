import numpy as np
from scipy.io.wavfile import write

from tools.codec import Codec

SAMPLE_RATE = 44100
BAUD_RATE = 200
FREQ_SPACE = 1000
FREQ_MARK = 2000


def fsk_encode(data, sample_rate, f0, f1, baud_rate):
    t = np.linspace(0, 1 / baud_rate, int(sample_rate / baud_rate), endpoint=False)
    signal = np.array([])

    for bit in data:
        if bit == 0:
            signal = np.concatenate((signal, np.sin(2 * np.pi * f0 * t)))
        else:
            signal = np.concatenate((signal, np.sin(2 * np.pi * f1 * t)))

    return signal


data = """\033[2J\033[H

    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ "Don't judge each day by the harvest you reap but by the seeds that you plant."   ┃
    ┃   - Robert Louis Stevenson, Scottish novelist, poet, essayist, and travel writer. ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""

# Generate data
codec = Codec()
data = codec.encode_string(data)

# Generate FSK signal
signal = fsk_encode(data, SAMPLE_RATE, FREQ_SPACE, FREQ_MARK, BAUD_RATE)

print("Sample per symbol: ", SAMPLE_RATE / BAUD_RATE)
print("Signal length: ", len(signal))
print("Signal duration: ", len(signal) / SAMPLE_RATE)

# Normalize signal
signal = np.int16(signal / np.max(np.abs(signal)) * 32767)

# Save signal to a WAV file
write("fsk_signal.wav", SAMPLE_RATE, signal)
