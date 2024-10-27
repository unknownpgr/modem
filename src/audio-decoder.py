import sys

import numpy as np
import pyaudio

from tools.codec import Codec
from tools.envelop_detector import EnvelopeDetector
from tools.frequency_detector import FrequencyDetector
from tools.symbol_decoder import SymbolDecoder

SAMPLE_RATE = 44100
BAUD_RATE = 200

frequency_detector = FrequencyDetector()
envelope_detector = EnvelopeDetector(127)
symbol_decoder = SymbolDecoder(sample_per_symbol=SAMPLE_RATE / BAUD_RATE, logging=False)
codec = Codec()

# Create audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=1,
)

while True:
    data = stream.read(1, exception_on_overflow=False)
    data = np.frombuffer(data, dtype=np.float32)[0]
    power_space, power_mark = frequency_detector.detect(data)
    bit = envelope_detector.detect(power_space, power_mark)

    bit = symbol_decoder.process(bit)
    byte = codec.decode(bit)
    if byte is not None:
        sys.stdout.buffer.write(byte)
        sys.stdout.flush()
