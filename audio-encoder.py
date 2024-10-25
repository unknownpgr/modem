import numpy as np
from scipy.io.wavfile import write

# 기본 파라미터 설정
sample_rate = 44100  # 샘플링 레이트
duration = 0.05  # 각 비트의 지속 시간 (초)
f0 = 4410  # 0에 대한 주파수 (Hz)
f1 = 8820  # 1에 대한 주파수 (Hz)

print("Sample per symbol: ", sample_rate * duration)


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


# Preamble
preamble = [0, 1] * 16

# IMPORTANT NOTE: ASCII code of first character must be larger than 127.
# Because if it is smaller than 127, especially when the first two bits are 01,
# it would be recognized as a preamble.
signal = encode_data("This is audio data encoding test.")
data = preamble + signal
print(len(data))

# FSK 신호 생성
signal = fsk_encode(data, sample_rate, f0, f1, duration)
print(len(signal) / sample_rate)

# 신호를 [-1, 1] 범위로 정규화
signal = np.int16(signal / np.max(np.abs(signal)) * 32767)

# WAV 파일로 저장
write("fsk_signal.wav", sample_rate, signal)
