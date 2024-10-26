class SymbolDecoder:

    def __init__(self, frame_per_symbol, logging=False):
        self.frame_per_symbol = frame_per_symbol
        self.counter = 0
        self.one_counter = 0
        self.zero_counter = 0
        self.none_counter = 0
        self.current_bit = None
        self.symbol_confidence = 0
        self.logging = logging

    def process(self, input):
        if self.logging:
            if input is None:
                print(".", end="", flush=True)
            else:
                print(input, end="", flush=True)

        # Update symbol_confidence
        if input is None:
            self.symbol_confidence -= 0
        else:
            self.symbol_confidence += 1
        if self.symbol_confidence < 3:
            self.symbol_confidence = 3
        if self.symbol_confidence > 10:
            self.symbol_confidence = 10

        # Symbol edge alignment
        if self.current_bit is not input:
            if self.current_bit is None:
                self.zero_counter = 0
                self.one_counter = 0
                self.none_counter = 0
                self.counter = 0
                self.current_bit = input
            else:
                if self.counter < self.frame_per_symbol / 2:
                    self.counter -= self.frame_per_symbol / self.symbol_confidence
                else:
                    self.counter += self.frame_per_symbol / self.symbol_confidence

        # Update counter
        if input is None:
            self.none_counter += 1
        elif input == 1:
            self.one_counter += 1
        else:
            self.zero_counter += 1
        self.counter += 1

        # If it is symbol boundary, decide the bit and reset the counters
        if self.counter >= self.frame_per_symbol:
            self.counter -= self.frame_per_symbol

            if self.none_counter > max(self.one_counter, self.zero_counter):
                output = None
            elif self.one_counter > self.zero_counter:
                output = 1
            else:
                output = 0

            self.one_counter = 0
            self.zero_counter = 0
            self.none_counter = 0
            self.current_bit = None

            if self.logging:
                print("==>", output)

            return output

        return None
