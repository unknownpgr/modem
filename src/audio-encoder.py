import os

import numpy as np
from scipy.io.wavfile import write

from codec import Codec

SAMPLE_RATE = 44100
BAUD_RATE = 1000
FREQ_SPACE = 6500
FREQ_MARK = 8000


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

    The Student

    At first, everything was still and quiet in the evening air. A student named Ivan Velikopolsky,
    a young man in a long coat, walked home, feeling troubled by the bleak cold and oppressive land
    scape around him. He felt as if he were a thousand years old and carrying the weight of all hum
    anity’s suffering on his shoulders.

    Ivan crossed the river and entered a village where he saw two women sitting by a campfire. He s
    topped to warm himself and began to talk with them. As they sat in the flickering firelight, Iv
    an spoke about a story he had learned in school — the story of Peter denying Jesus three times.
    He recounted how Peter, feeling the bitter chill of the night, had followed Jesus to the high 
    priest's palace, where he warmed himself by a fire. When someone recognized him as a disciple o
    f Jesus, Peter, out of fear, denied knowing Him. This happened three times, just as Jesus had p
    redicted, and Peter realized his weakness and wept.

    As Ivan told the story, he saw the faces of the two women before him change. He could feel the
    y were moved, as if they were reliving the ancient sorrow that Peter felt. The older woman, Vas
    i lisa, began to cry, and her expression filled with the sorrow and understanding that comes wi
    th age and hardship.

    In that moment, Ivan realized that he had touched something universal in them. He felt that th
    e world, although filled with suffering, was also connected through stories and shared experien
    ces. He had witnessed a profound truth — that human hearts could resonate with ancient tales of
    sorrow and redemption, transcending time and culture.

                                                    - Anton Chekhov -

"""

# Generate data
codec = Codec()
data = codec.encode(data)
print("".join(str(bit) for bit in data))

# Generate FSK signal
signal = fsk_encode(data, SAMPLE_RATE, FREQ_SPACE, FREQ_MARK, BAUD_RATE)

print("Sample per symbol: ", SAMPLE_RATE / BAUD_RATE)
print("Signal length: ", len(signal))
print("Signal duration: ", len(signal) / SAMPLE_RATE)

# Normalize signal
signal = np.int16(signal / np.max(np.abs(signal)) * 32767)

# Delete all existing *.wav file
for file in os.listdir():
    if file.endswith(".wav"):
        os.remove(file)

# Save signal to a WAV file
filename = f"signal_{BAUD_RATE}bps.wav"
write(filename, SAMPLE_RATE, signal)
