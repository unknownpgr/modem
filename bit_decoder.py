FRAME_PER_SYMBOL = 5

counter = 0

one_counter = 0
zero_counter = 0
none_counter = 0

current_bit = None
symbol_confidence = 0


def filter_input(input):
    # if input is not None:
    #     print(input, end="", flush=True)
    # else:
    #     print("?", end="", flush=True)

    global counter
    global one_counter
    global zero_counter
    global none_counter
    global current_bit
    global symbol_confidence

    # Update symbol_confidence
    if input is None:
        symbol_confidence -= 0
    else:
        symbol_confidence += 1
    if symbol_confidence < 0:
        symbol_confidence = 0
    if symbol_confidence > 10:
        symbol_confidence = 10

    # Edge alignment
    if current_bit is not input:
        if current_bit is None:
            zero_counter = 0
            one_counter = 0
            none_counter = 0
            counter = 0
            current_bit = input
        else:
            if counter < FRAME_PER_SYMBOL / 2:
                counter -= FRAME_PER_SYMBOL / symbol_confidence
            else:
                counter += FRAME_PER_SYMBOL / symbol_confidence

    # Update counter
    if input is None:
        none_counter += 1
    elif input == 1:
        one_counter += 1
    else:
        zero_counter += 1
    counter += 1

    # If it is symbol boundary, decide the bit and reset counters
    if counter >= FRAME_PER_SYMBOL:
        counter -= FRAME_PER_SYMBOL

        if none_counter > max(one_counter, zero_counter):
            output = None
        elif one_counter > zero_counter:
            output = 1
        else:
            output = 0

        # print("", none_counter, one_counter, zero_counter, sep=", ", end=" -> ")
        # print(output)

        one_counter = 0
        zero_counter = 0
        none_counter = 0
        current_bit = None

        return output

    return None
