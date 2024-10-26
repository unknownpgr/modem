import numpy as np
from scipy.io.wavfile import write

# 기본 파라미터 설정
SAMPLE_RATE = 44100
DURATION = 0.02
FREQ_SPACE = 1000
FREQ_MARK = 2000

print("Sample per symbol: ", SAMPLE_RATE * DURATION)


def fsk_encode(data, sample_rate, f0, f1, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.array([])

    for bit in data:
        if bit == 0:
            signal = np.concatenate((signal, np.sin(2 * np.pi * f0 * t)))
        else:
            signal = np.concatenate((signal, np.sin(2 * np.pi * f1 * t)))

    return signal


def encode_data(string):
    data = []
    for char in string:
        byte = ord(char)
        for i in range(8):
            data.append((byte >> i) & 1)
    return data


data = (
    '\n\n  "You only live once but if you do it right, once is enough." - Mae West\n\n'
)

# Generate data
sync_signal = [0, 1] * 16
preamble = [0, 0, 0, 1, 0, 0, 0, 1] * 2
signal = encode_data(data)
data = sync_signal + preamble + signal

# Generate FSK signal
signal = fsk_encode(data, SAMPLE_RATE, FREQ_SPACE, FREQ_MARK, DURATION)
print("Signal length: ", len(signal))
print("Signal duration: ", len(signal) / SAMPLE_RATE)

# Normalize signal
signal = np.int16(signal / np.max(np.abs(signal)) * 32767)

# Save signal to a WAV file
write("fsk_signal.wav", SAMPLE_RATE, signal)
