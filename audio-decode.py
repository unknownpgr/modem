import pyaudio
import numpy as np
from scipy.fftpack import fft
from symbol_decoder import SymbolDecoder

SAMPLE_RATE = 44100
DURATION = 0.05
FRAME_SIZE = 441
FRAME_PER_SYMBOL = int(SAMPLE_RATE * DURATION) // FRAME_SIZE

SPACE_FREQ = 4410
MARK_FREQ = 8820


def detect_fsk_signal(signal, rate):
    # FFT를 사용하여 주파수 스펙트럼을 분석
    fft_data = fft(signal)
    freqs = np.fft.fftfreq(len(fft_data), d=1 / rate)

    # Filter out the signal
    space_freq_range = (SPACE_FREQ - 100, SPACE_FREQ + 100)
    mark_freq_range = (MARK_FREQ - 100, MARK_FREQ + 100)
    space_freq_idx = np.where(
        (freqs >= space_freq_range[0]) & (freqs <= space_freq_range[1])
    )[0]
    mark_freq_idx = np.where(
        (freqs >= mark_freq_range[0]) & (freqs <= mark_freq_range[1])
    )[0]

    space_power = np.sum(np.abs(fft_data[space_freq_idx]) ** 2)
    mark_power = np.sum(np.abs(fft_data[mark_freq_idx]) ** 2)

    if space_power < 0.1 and mark_power < 0.1:
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

decoder = SymbolDecoder(FRAME_PER_SYMBOL)
preamble = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
preamble_buffer = []
is_preamble = False
byte_buffer = []

while True:
    # 오디오 데이터 읽기
    data = stream.read(FRAME_SIZE)
    data = np.frombuffer(data, dtype=np.float32)

    # FSK 신호 감지
    bit = detect_fsk_signal(data, SAMPLE_RATE)
    bit = decoder.process(bit)
    # continue

    if bit is not None:
        preamble_buffer.append(bit)
        if len(preamble_buffer) > len(preamble):
            preamble_buffer.pop(0)
        if preamble_buffer == preamble:
            is_preamble = True
            byte_buffer = []
            continue
    if is_preamble and bit is not None:
        byte_buffer.append(bit)
        if len(byte_buffer) == 8:
            byte = 0
            for i in range(8):
                byte |= byte_buffer[i] << i
            print(chr(byte), end="", flush=True)
            byte_buffer = []
