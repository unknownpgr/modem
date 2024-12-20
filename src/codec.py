import numpy as np


class Encoding8b10b:
    def __init__(self):
        self.mapping = [
            (0, [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),
            (0, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),
            (0, [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]),
            (0, [0, 0, 1, 0, 1, 0, 1, 0, 1, 1]),
            (0, [0, 1, 0, 0, 1, 0, 1, 0, 1, 1]),
            (0, [0, 0, 1, 1, 0, 0, 1, 0, 1, 1]),
            (0, [0, 1, 0, 1, 0, 0, 1, 0, 1, 1]),
            (0, [1, 0, 0, 1, 0, 0, 1, 0, 1, 1]),
            (0, [0, 0, 1, 0, 1, 1, 0, 0, 1, 1]),
            (0, [0, 1, 0, 0, 1, 1, 0, 0, 1, 1]),
            (0, [0, 0, 1, 1, 0, 1, 0, 0, 1, 1]),
            (0, [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]),
            (0, [1, 0, 0, 1, 0, 1, 0, 0, 1, 1]),
            (0, [0, 1, 1, 0, 0, 1, 0, 0, 1, 1]),
            (0, [1, 0, 1, 0, 0, 1, 0, 0, 1, 1]),
            (0, [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]),
            (0, [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]),
            (0, [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]),
            (0, [0, 1, 0, 1, 0, 0, 1, 1, 0, 1]),
            (0, [1, 0, 0, 1, 0, 0, 1, 1, 0, 1]),
            (0, [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]),
            (0, [0, 1, 0, 0, 1, 1, 0, 1, 0, 1]),
            (0, [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]),
            (0, [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]),
            (0, [0, 1, 1, 0, 0, 1, 0, 1, 0, 1]),
            (0, [1, 0, 1, 0, 0, 1, 0, 1, 0, 1]),
            (0, [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]),
            (0, [1, 0, 0, 1, 1, 0, 0, 1, 0, 1]),
            (0, [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]),
            (0, [1, 0, 1, 0, 1, 0, 0, 1, 0, 1]),
            (0, [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]),
            (0, [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]),
            (0, [0, 1, 0, 1, 0, 1, 1, 0, 0, 1]),
            (0, [1, 0, 0, 1, 0, 1, 1, 0, 0, 1]),
            (0, [0, 1, 1, 0, 0, 1, 1, 0, 0, 1]),
            (0, [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]),
            (0, [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]),
            (0, [1, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
            (0, [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]),
            (0, [1, 0, 1, 0, 1, 0, 1, 0, 0, 1]),
            (0, [1, 1, 0, 0, 1, 0, 1, 0, 0, 1]),
            (0, [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]),
            (0, [1, 1, 0, 1, 0, 0, 1, 0, 0, 1]),
            (0, [0, 0, 1, 0, 1, 1, 0, 1, 1, 0]),
            (0, [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]),
            (0, [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]),
            (0, [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]),
            (0, [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]),
            (0, [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]),
            (0, [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]),
            (0, [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]),
            (0, [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]),
            (0, [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]),
            (0, [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]),
            (0, [1, 1, 0, 0, 1, 0, 0, 1, 1, 0]),
            (0, [0, 0, 1, 1, 0, 1, 1, 0, 1, 0]),
            (0, [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]),
            (0, [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]),
            (0, [0, 1, 1, 0, 0, 1, 1, 0, 1, 0]),
            (0, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]),
            (0, [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]),
            (0, [1, 0, 0, 1, 1, 0, 1, 0, 1, 0]),
            (0, [0, 1, 1, 0, 1, 0, 1, 0, 1, 0]),
            (0, [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]),
            (0, [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]),
            (0, [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]),
            (0, [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]),
            (0, [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]),
            (0, [1, 1, 0, 0, 1, 1, 0, 0, 1, 0]),
            (0, [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]),
            (0, [1, 1, 0, 1, 0, 1, 0, 0, 1, 0]),
            (0, [0, 1, 0, 1, 1, 0, 1, 1, 0, 0]),
            (0, [1, 0, 0, 1, 1, 0, 1, 1, 0, 0]),
            (0, [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]),
            (0, [1, 0, 1, 0, 1, 0, 1, 1, 0, 0]),
            (0, [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]),
            (0, [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]),
            (0, [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]),
            (0, [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]),
            (0, [1, 0, 1, 0, 1, 1, 0, 1, 0, 0]),
            (0, [1, 1, 0, 0, 1, 1, 0, 1, 0, 0]),
            (0, [1, 0, 1, 1, 0, 1, 0, 1, 0, 0]),
            (0, [1, 1, 0, 1, 0, 1, 0, 1, 0, 0]),
            (0, [1, 1, 0, 1, 1, 0, 0, 1, 0, 0]),
            (0, [0, 0, 0, 1, 0, 1, 0, 1, 1, 1]),
            (0, [0, 0, 1, 0, 0, 1, 0, 1, 1, 1]),
            (0, [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]),
            (0, [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]),
            (0, [0, 0, 1, 0, 1, 0, 0, 1, 1, 1]),
            (0, [0, 1, 0, 0, 1, 0, 0, 1, 1, 1]),
            (0, [1, 0, 0, 0, 1, 0, 0, 1, 1, 1]),
            (0, [0, 0, 1, 1, 0, 0, 0, 1, 1, 1]),
            (0, [0, 1, 0, 1, 0, 0, 0, 1, 1, 1]),
            (0, [1, 0, 0, 1, 0, 0, 0, 1, 1, 1]),
            (0, [0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
            (0, [0, 1, 0, 0, 0, 1, 1, 0, 1, 1]),
            (0, [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]),
            (0, [1, 0, 0, 0, 1, 0, 1, 0, 1, 1]),
            (0, [0, 1, 1, 0, 0, 0, 1, 0, 1, 1]),
            (0, [1, 0, 1, 0, 0, 0, 1, 0, 1, 1]),
            (0, [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]),
            (0, [1, 0, 0, 0, 1, 1, 0, 0, 1, 1]),
            (0, [1, 1, 0, 0, 0, 1, 0, 0, 1, 1]),
            (0, [0, 0, 1, 1, 1, 0, 0, 0, 1, 1]),
            (0, [0, 1, 0, 1, 1, 0, 0, 0, 1, 1]),
            (0, [1, 0, 0, 1, 1, 0, 0, 0, 1, 1]),
            (0, [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]),
            (0, [1, 0, 1, 0, 1, 0, 0, 0, 1, 1]),
            (0, [1, 1, 0, 0, 1, 0, 0, 0, 1, 1]),
            (0, [0, 0, 0, 1, 0, 1, 1, 1, 0, 1]),
            (0, [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]),
            (0, [0, 1, 0, 0, 0, 1, 1, 1, 0, 1]),
            (0, [0, 0, 0, 1, 1, 0, 1, 1, 0, 1]),
            (0, [1, 0, 0, 0, 1, 0, 1, 1, 0, 1]),
            (0, [0, 1, 1, 0, 0, 0, 1, 1, 0, 1]),
            (0, [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]),
            (0, [0, 0, 0, 1, 1, 1, 0, 1, 0, 1]),
            (0, [1, 0, 0, 0, 1, 1, 0, 1, 0, 1]),
            (0, [1, 1, 0, 0, 0, 1, 0, 1, 0, 1]),
            (0, [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]),
            (0, [0, 1, 1, 1, 0, 0, 0, 1, 0, 1]),
            (0, [1, 0, 1, 1, 0, 0, 0, 1, 0, 1]),
            (0, [1, 1, 0, 1, 0, 0, 0, 1, 0, 1]),
            (0, [0, 0, 1, 0, 1, 1, 1, 0, 0, 1]),
            (0, [0, 1, 0, 0, 1, 1, 1, 0, 0, 1]),
            (0, [1, 0, 0, 0, 1, 1, 1, 0, 0, 1]),
            (0, [1, 1, 0, 0, 0, 1, 1, 0, 0, 1]),
            (0, [0, 0, 1, 1, 1, 0, 1, 0, 0, 1]),
            (0, [0, 1, 1, 1, 0, 0, 1, 0, 0, 1]),
            (0, [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]),
            (0, [0, 1, 0, 1, 1, 1, 0, 0, 0, 1]),
            (0, [1, 0, 0, 1, 1, 1, 0, 0, 0, 1]),
            (0, [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]),
            (0, [1, 0, 1, 0, 1, 1, 0, 0, 0, 1]),
            (0, [1, 1, 0, 0, 1, 1, 0, 0, 0, 1]),
            (0, [0, 1, 1, 1, 0, 1, 0, 0, 0, 1]),
            (0, [1, 0, 1, 1, 0, 1, 0, 0, 0, 1]),
            (0, [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]),
            (0, [1, 1, 1, 0, 0, 1, 0, 0, 0, 1]),
            (0, [0, 0, 0, 1, 1, 0, 1, 1, 1, 0]),
            (0, [0, 0, 1, 0, 1, 0, 1, 1, 1, 0]),
            (0, [0, 1, 0, 0, 1, 0, 1, 1, 1, 0]),
            (0, [1, 0, 0, 0, 1, 0, 1, 1, 1, 0]),
            (0, [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]),
            (0, [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]),
            (0, [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]),
            (0, [0, 1, 1, 0, 0, 0, 1, 1, 1, 0]),
            (0, [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]),
            (0, [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]),
            (0, [1, 0, 0, 0, 1, 1, 0, 1, 1, 0]),
            (0, [1, 1, 0, 0, 0, 1, 0, 1, 1, 0]),
            (0, [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]),
            (0, [0, 1, 1, 1, 0, 0, 0, 1, 1, 0]),
            (0, [1, 0, 1, 1, 0, 0, 0, 1, 1, 0]),
            (0, [1, 1, 0, 1, 0, 0, 0, 1, 1, 0]),
            (0, [0, 0, 1, 0, 1, 1, 1, 0, 1, 0]),
            (0, [0, 1, 0, 0, 1, 1, 1, 0, 1, 0]),
            (0, [1, 0, 0, 0, 1, 1, 1, 0, 1, 0]),
            (0, [1, 1, 0, 0, 0, 1, 1, 0, 1, 0]),
            (0, [0, 0, 1, 1, 1, 0, 1, 0, 1, 0]),
            (0, [0, 1, 1, 1, 0, 0, 1, 0, 1, 0]),
            (0, [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]),
            (0, [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]),
            (0, [1, 0, 0, 1, 1, 1, 0, 0, 1, 0]),
            (0, [0, 1, 1, 1, 0, 1, 0, 0, 1, 0]),
            (0, [1, 1, 1, 0, 0, 1, 0, 0, 1, 0]),
            (0, [1, 0, 1, 1, 1, 0, 0, 0, 1, 0]),
            (0, [1, 1, 0, 1, 1, 0, 0, 0, 1, 0]),
            (0, [1, 1, 1, 0, 1, 0, 0, 0, 1, 0]),
            (0, [0, 0, 1, 1, 0, 1, 1, 1, 0, 0]),
            (0, [0, 1, 0, 1, 0, 1, 1, 1, 0, 0]),
            (0, [1, 0, 0, 1, 0, 1, 1, 1, 0, 0]),
            (0, [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]),
            (0, [1, 0, 1, 0, 0, 1, 1, 1, 0, 0]),
            (0, [1, 1, 0, 0, 0, 1, 1, 1, 0, 0]),
            (0, [0, 0, 1, 1, 1, 0, 1, 1, 0, 0]),
            (0, [0, 1, 1, 1, 0, 0, 1, 1, 0, 0]),
            (0, [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]),
            (0, [0, 1, 0, 1, 1, 1, 0, 1, 0, 0]),
            (0, [1, 0, 0, 1, 1, 1, 0, 1, 0, 0]),
            (0, [0, 1, 1, 1, 0, 1, 0, 1, 0, 0]),
            (0, [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]),
            (0, [1, 0, 1, 1, 1, 0, 0, 1, 0, 0]),
            (0, [1, 1, 1, 0, 1, 0, 0, 1, 0, 0]),
            (0, [0, 1, 1, 0, 1, 1, 1, 0, 0, 0]),
            (0, [1, 0, 1, 0, 1, 1, 1, 0, 0, 0]),
            (0, [1, 1, 0, 0, 1, 1, 1, 0, 0, 0]),
            (0, [0, 1, 1, 1, 0, 1, 1, 0, 0, 0]),
            (0, [1, 0, 1, 1, 0, 1, 1, 0, 0, 0]),
            (0, [1, 1, 0, 1, 0, 1, 1, 0, 0, 0]),
            (0, [1, 1, 1, 0, 0, 1, 1, 0, 0, 0]),
            (0, [1, 0, 1, 1, 1, 0, 1, 0, 0, 0]),
            (0, [1, 1, 0, 1, 1, 0, 1, 0, 0, 0]),
            (0, [1, 1, 1, 0, 1, 0, 1, 0, 0, 0]),
            (2, [0, 0, 1, 1, 0, 1, 1, 0, 1, 1]),
            (2, [0, 1, 0, 1, 0, 1, 1, 0, 1, 1]),
            (2, [1, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
            (2, [0, 1, 1, 0, 0, 1, 1, 0, 1, 1]),
            (2, [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]),
            (2, [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]),
            (2, [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]),
            (2, [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]),
            (2, [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]),
            (2, [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]),
            (2, [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]),
            (2, [1, 1, 0, 1, 0, 0, 1, 0, 1, 1]),
            (2, [0, 1, 1, 0, 1, 1, 0, 0, 1, 1]),
            (2, [1, 0, 1, 0, 1, 1, 0, 0, 1, 1]),
            (2, [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]),
            (2, [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]),
            (2, [1, 1, 0, 1, 0, 1, 0, 0, 1, 1]),
            (2, [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]),
            (2, [1, 0, 0, 1, 1, 0, 1, 1, 0, 1]),
            (2, [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]),
            (2, [1, 0, 1, 0, 1, 0, 1, 1, 0, 1]),
            (2, [1, 1, 0, 0, 1, 0, 1, 1, 0, 1]),
            (2, [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]),
            (2, [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]),
            (2, [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]),
            (2, [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]),
            (2, [1, 1, 0, 0, 1, 1, 0, 1, 0, 1]),
            (2, [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]),
            (2, [1, 1, 0, 1, 0, 1, 0, 1, 0, 1]),
            (2, [1, 1, 0, 1, 1, 0, 0, 1, 0, 1]),
            (2, [1, 0, 1, 1, 0, 1, 1, 0, 0, 1]),
            (2, [1, 1, 0, 1, 0, 1, 1, 0, 0, 1]),
            (2, [1, 1, 0, 1, 1, 0, 1, 0, 0, 1]),
            (2, [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]),
            (2, [1, 0, 1, 0, 1, 1, 0, 1, 1, 0]),
            (2, [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]),
            (2, [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]),
            (2, [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]),
            (2, [1, 1, 0, 1, 1, 0, 0, 1, 1, 0]),
            (2, [1, 0, 1, 1, 0, 1, 1, 0, 1, 0]),
            (2, [1, 1, 0, 1, 0, 1, 1, 0, 1, 0]),
            (2, [1, 1, 0, 1, 1, 0, 1, 0, 1, 0]),
            (2, [1, 1, 0, 1, 1, 0, 1, 1, 0, 0]),
            (2, [0, 0, 0, 1, 1, 1, 0, 1, 1, 1]),
            (2, [0, 0, 1, 0, 1, 1, 0, 1, 1, 1]),
            (2, [0, 1, 0, 0, 1, 1, 0, 1, 1, 1]),
            (2, [1, 0, 0, 0, 1, 1, 0, 1, 1, 1]),
            (2, [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]),
            (2, [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]),
            (2, [1, 0, 0, 1, 0, 1, 0, 1, 1, 1]),
            (2, [0, 1, 1, 0, 0, 1, 0, 1, 1, 1]),
            (2, [1, 0, 1, 0, 0, 1, 0, 1, 1, 1]),
            (2, [1, 1, 0, 0, 0, 1, 0, 1, 1, 1]),
            (2, [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]),
            (2, [0, 1, 0, 1, 1, 0, 0, 1, 1, 1]),
            (2, [1, 0, 0, 1, 1, 0, 0, 1, 1, 1]),
            (2, [0, 1, 1, 0, 1, 0, 0, 1, 1, 1]),
            (2, [1, 0, 1, 0, 1, 0, 0, 1, 1, 1]),
            (2, [1, 1, 0, 0, 1, 0, 0, 1, 1, 1]),
            (2, [0, 1, 1, 1, 0, 0, 0, 1, 1, 1]),
            (2, [1, 0, 1, 1, 0, 0, 0, 1, 1, 1]),
            (2, [1, 1, 0, 1, 0, 0, 0, 1, 1, 1]),
            (2, [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]),
            (2, [0, 1, 0, 0, 1, 1, 1, 0, 1, 1]),
            (2, [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]),
            (2, [1, 1, 0, 0, 0, 1, 1, 0, 1, 1]),
            (2, [0, 0, 1, 1, 1, 0, 1, 0, 1, 1]),
            (2, [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]),
            (2, [1, 1, 1, 0, 0, 0, 1, 0, 1, 1]),
            (2, [0, 1, 0, 1, 1, 1, 0, 0, 1, 1]),
            (2, [1, 0, 0, 1, 1, 1, 0, 0, 1, 1]),
            (2, [0, 1, 1, 1, 0, 1, 0, 0, 1, 1]),
            (2, [1, 1, 1, 0, 0, 1, 0, 0, 1, 1]),
            (2, [1, 0, 1, 1, 1, 0, 0, 0, 1, 1]),
            (2, [1, 1, 0, 1, 1, 0, 0, 0, 1, 1]),
            (2, [1, 1, 1, 0, 1, 0, 0, 0, 1, 1]),
            (2, [0, 0, 1, 1, 0, 1, 1, 1, 0, 1]),
            (2, [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]),
            (2, [1, 0, 0, 1, 0, 1, 1, 1, 0, 1]),
            (2, [0, 1, 1, 0, 0, 1, 1, 1, 0, 1]),
            (2, [1, 0, 1, 0, 0, 1, 1, 1, 0, 1]),
            (2, [1, 1, 0, 0, 0, 1, 1, 1, 0, 1]),
            (2, [0, 0, 1, 1, 1, 0, 1, 1, 0, 1]),
            (2, [0, 1, 1, 1, 0, 0, 1, 1, 0, 1]),
            (2, [1, 1, 1, 0, 0, 0, 1, 1, 0, 1]),
            (2, [0, 1, 0, 1, 1, 1, 0, 1, 0, 1]),
            (2, [1, 0, 0, 1, 1, 1, 0, 1, 0, 1]),
            (2, [0, 1, 1, 1, 0, 1, 0, 1, 0, 1]),
            (2, [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]),
            (2, [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]),
            (2, [1, 1, 1, 0, 1, 0, 0, 1, 0, 1]),
            (2, [0, 1, 1, 0, 1, 1, 1, 0, 0, 1]),
            (2, [1, 0, 1, 0, 1, 1, 1, 0, 0, 1]),
            (2, [1, 1, 0, 0, 1, 1, 1, 0, 0, 1]),
            (2, [0, 1, 1, 1, 0, 1, 1, 0, 0, 1]),
            (2, [1, 1, 1, 0, 0, 1, 1, 0, 0, 1]),
            (2, [1, 0, 1, 1, 1, 0, 1, 0, 0, 1]),
            (2, [1, 1, 1, 0, 1, 0, 1, 0, 0, 1]),
            (2, [1, 1, 0, 1, 1, 1, 0, 0, 0, 1]),
            (2, [1, 1, 1, 0, 1, 1, 0, 0, 0, 1]),
            (2, [0, 0, 1, 1, 1, 0, 1, 1, 1, 0]),
            (2, [0, 1, 0, 1, 1, 0, 1, 1, 1, 0]),
            (2, [1, 0, 0, 1, 1, 0, 1, 1, 1, 0]),
            (2, [0, 1, 1, 0, 1, 0, 1, 1, 1, 0]),
            (2, [1, 0, 1, 0, 1, 0, 1, 1, 1, 0]),
            (2, [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]),
            (2, [0, 1, 1, 1, 0, 0, 1, 1, 1, 0]),
            (2, [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]),
            (2, [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]),
            (2, [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]),
            (2, [0, 1, 0, 1, 1, 1, 0, 1, 1, 0]),
            (2, [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]),
            (2, [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]),
            (2, [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]),
            (2, [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]),
            (2, [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]),
            (2, [0, 1, 1, 0, 1, 1, 1, 0, 1, 0]),
            (2, [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]),
            (2, [1, 1, 0, 0, 1, 1, 1, 0, 1, 0]),
            (2, [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]),
            (2, [1, 1, 1, 0, 0, 1, 1, 0, 1, 0]),
            (2, [1, 0, 1, 1, 1, 0, 1, 0, 1, 0]),
            (2, [1, 1, 1, 0, 1, 0, 1, 0, 1, 0]),
            (2, [1, 1, 0, 1, 1, 1, 0, 0, 1, 0]),
            (2, [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]),
            (2, [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]),
            (2, [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]),
            (2, [1, 1, 0, 1, 0, 1, 1, 1, 0, 0]),
            (2, [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]),
            (2, [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]),
            (2, [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]),
            (2, [1, 1, 0, 1, 1, 1, 0, 1, 0, 0]),
            (2, [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]),
            (2, [1, 1, 1, 0, 1, 1, 1, 0, 0, 0]),
        ]

        self.reverse_mapping = {}
        for i, (balance, bits) in enumerate(self.mapping):
            self.reverse_mapping[self.__bits_to_number(bits)] = i
            if balance != 0:
                bits = self.__invert_bits(bits)
                self.reverse_mapping[self.__bits_to_number(bits)] = i

    def __invert_bits(self, bits):
        return [1 - bit for bit in bits]

    def __bits_to_number(self, bits):
        number = 0
        for bit in bits:
            number = (number << 1) | bit
        return number

    def encode(self, data):
        if isinstance(data, str):
            data = data.encode("utf-8")
        bits = []
        total_balance = 0
        for byte in data:
            balance, byte_bits = self.mapping[byte]
            if total_balance > 0 and balance > 0:
                total_balance -= balance
                bits.extend(self.__invert_bits(byte_bits))
            else:
                total_balance += balance
                bits.extend(byte_bits)
        return bits

    def decode(self, bits):
        assert len(bits) % 10 == 0
        buf = bytearray()
        for i in range(0, len(bits), 10):
            number = self.__bits_to_number(bits[i : i + 10])
            try:
                decoded = self.reverse_mapping[number]
            except KeyError:
                return None
            decoded = decoded & 0xFF
            buf.append(decoded)
        return buf


class Codec:
    def __init__(self, sync_length=500):
        self.sync_length = sync_length
        self.preamble = [1, 0, 0, 1, 0, 0, 0, 1] * 2
        self.preamble_buffer = []
        self.bit_buffer = []
        self.encoding = Encoding8b10b()

    def __add_preamble(self, bits):
        return [0, 1] * self.sync_length + self.preamble + bits

    def encode(self, data):
        data = self.encoding.encode(data)
        return self.__add_preamble(data)

    def decode(self, bit):
        if bit is None:
            return None

        # Clear byte buffer when preamble is detected
        self.preamble_buffer.append(bit)
        if len(self.preamble_buffer) > len(self.preamble):
            self.preamble_buffer.pop(0)
        if self.preamble_buffer == self.preamble:
            self.bit_buffer = []
            print("\n\nPreamble detected\n")
            return None

        # Decode byte when 10 bits are received
        self.bit_buffer.append(bit)
        if len(self.bit_buffer) == 10:
            decoded = self.encoding.decode(self.bit_buffer)
            self.bit_buffer = []
            if decoded is not None:
                return decoded
        return None
