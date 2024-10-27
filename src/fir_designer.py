import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, freqz


class FilterDesigner:

    def design_filter(sample_rate, f_select, f_band, numtaps):
        f_pass1 = f_select - f_band / 2
        f_pass2 = f_select + f_band / 2
        fir_coeff = firwin(numtaps, [f_pass1, f_pass2], pass_zero=False, fs=sample_rate)
        return fir_coeff

    def evaluate_q_factor(sample_rate, fir_coeff):
        # Calculate frequency response
        w, h = freqz(fir_coeff, worN=8000, fs=sample_rate)

        # Calculate Q factor from frequency response
        h_max = np.max(abs(h))
        f_max = w[np.argmax(abs(h))]
        f_3db = w[np.argmax(abs(h) >= h_max / np.sqrt(2))]
        band_3db = (f_max - f_3db) * 2

        if band_3db == 0:
            return 0

        Q = f_max / band_3db

        return Q

    def design_filter_with_q_factor(sample_rate, f_select, q_factor):
        numtaps_min = 1
        numtaps_max = 21

        while True:
            fir_coeff = FilterDesigner.design_filter(
                sample_rate, f_select, f_select / q_factor, numtaps_max
            )
            Q = FilterDesigner.evaluate_q_factor(fir_coeff)
            if Q < q_factor:
                numtaps_max = numtaps_max * 2
            else:
                break

        while numtaps_max - numtaps_min > 1:
            numtaps = (numtaps_max + numtaps_min) // 2
            fir_coeff = FilterDesigner.design_filter(
                sample_rate, f_select, f_select / q_factor, numtaps
            )
            Q = FilterDesigner.evaluate_q_factor(fir_coeff)
            if Q < q_factor:
                numtaps_min = numtaps
            else:
                numtaps_max = numtaps

        fir_coeff = FilterDesigner.design_filter(
            sample_rate, f_select, f_select / q_factor, numtaps_min
        )
        return fir_coeff, numtaps_min, Q

    def design_filter_with_numtaps(sample_rate, f_select, numtaps):
        fir_coeff = FilterDesigner.design_filter(sample_rate, f_select, 0.01, numtaps)
        Q = FilterDesigner.evaluate_q_factor(sample_rate, fir_coeff)
        return fir_coeff, numtaps, Q


if __name__ == "__main__":
    while True:
        selected_frequency = int(input("Enter the selected frequency: "))
        try:
            selected_frequency = float(selected_frequency)
        except ValueError:
            print("Please enter a valid number")
            continue

        numtaps = int(input("Enter the number of taps: "))
        try:
            numtaps = int(numtaps)
            if numtaps % 2 == 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid number")
            continue

        fir_coeff, numtaps, Q = FilterDesigner.design_filter_with_numtaps(
            44100, selected_frequency, numtaps
        )
        print(f"Number of taps: {numtaps}")
        print(f"Q factor: {Q}")
        print("FIR coefficients: ")
        print("[" + ",".join([str(x) for x in fir_coeff]) + "]")
