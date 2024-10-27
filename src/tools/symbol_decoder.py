class SymbolDecoder:

    def __init__(self, frame_per_symbol, logging=False):
        self.frame_per_symbol = frame_per_symbol
        self.counter = 0
        self.vco_input = 1
        self.one_counter = 0
        self.zero_counter = 0
        self.none_counter = 0
        self.current_bit = None
        self.logging = logging

    def process(self, input):
        if self.logging:
            if input is None:
                print(".", end="", flush=True)
            elif input == 0:
                print("_", end="", flush=True)
            else:
                print("-", end="", flush=True)

        # Symbol edge alignment with software PLL
        if self.current_bit is not input:
            if self.current_bit is None:
                self.zero_counter = 0
                self.one_counter = 0
                self.none_counter = 0
                self.counter = 0
                self.current_bit = input
            else:
                self.current_bit = input
                if self.logging:
                    print("◼️", end="")
                if self.counter < self.frame_per_symbol * 0.5:
                    self.vco_input = -0.01
                elif self.counter > self.frame_per_symbol * 0.5:
                    self.vco_input = 0.01

        # Update counter
        if input is None:
            self.none_counter += 1
        elif input == 1:
            self.one_counter += 1
        else:
            self.zero_counter += 1
        self.counter += 1 + self.vco_input

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
                print(f"{self.vco_input:.2f}", end="")

            return output

        return None
