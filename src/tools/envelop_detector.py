import numpy as np


class EnvelopeDetector:
    def __init__(self, filter_size):
        self.buffer_space = np.zeros(filter_size)
        self.buffer_power = np.zeros(filter_size)

    def detect(self, sample_space, sample_power):
        self.buffer_space = np.roll(self.buffer_space, 1)
        self.buffer_space[0] = abs(sample_space)
        self.buffer_power = np.roll(self.buffer_power, 1)
        self.buffer_power[0] = abs(sample_power)

        filtered_space = np.mean(self.buffer_space)
        filtered_power = np.mean(self.buffer_power)

        if filtered_space < 0.0001 and filtered_power < 0.0001:
            return None

        if filtered_space > filtered_power:
            return 0
        else:
            return 1
