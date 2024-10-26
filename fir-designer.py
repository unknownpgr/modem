from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt
import numpy as np


def design_filter(f_s, f_select, f_band, numtaps):
    f_pass1 = f_select - f_band / 2
    f_pass2 = f_select + f_band / 2
    fir_coeff = firwin(numtaps, [f_pass1, f_pass2], pass_zero=False, fs=f_s)
    return fir_coeff


def evaluate_q_factor(fir_coeff):
    # Calculate frequency response
    w, h = freqz(fir_coeff, worN=8000, fs=f_s)

    # Calculate Q factor from frequency response
    h_max = np.max(abs(h))
    f_max = w[np.argmax(abs(h))]
    f_3db = w[np.argmax(abs(h) >= h_max / np.sqrt(2))]
    band_3db = (f_max - f_3db) * 2

    if band_3db == 0:
        return 0

    Q = f_max / band_3db

    return Q


def design_filter_with_q_factor(f_s, f_select, q_factor):
    numtaps_min = 1
    numtaps_max = 21

    while True:
        fir_coeff = design_filter(f_s, f_select, f_select / q_factor, numtaps_max)
        Q = evaluate_q_factor(fir_coeff)
        if Q < q_factor:
            numtaps_max = numtaps_max * 2
        else:
            break

    while numtaps_max - numtaps_min > 1:
        numtaps = (numtaps_max + numtaps_min) // 2
        fir_coeff = design_filter(f_s, f_select, f_select / q_factor, numtaps)
        Q = evaluate_q_factor(fir_coeff)
        if Q < q_factor:
            numtaps_min = numtaps
        else:
            numtaps_max = numtaps

    fir_coeff = design_filter(f_s, f_select, f_select / q_factor, numtaps_min)
    return fir_coeff, numtaps_min, Q


def get_envelope(signal, numtaps):
    signal = np.abs(signal)
    fir_coeff = np.ones(numtaps) / numtaps
    return np.convolve(signal, fir_coeff, mode="same")


def encode_data(f_s, baud_rate, bits):
    length = len(bits) * f_s // baud_rate
    selection = np.zeros(length)
    for i in range(length):
        selection[i] = bits[int(i * baud_rate / f_s)]
    return selection


# Filter design
f_s = 44100
f_select = 1000
q_factor = 2
fir_coeff, numtaps, Q = design_filter_with_q_factor(f_s, f_select, q_factor)
print(f"Number of taps: {numtaps}")
print(f"Q factor: {Q}")

# Frequency response
w, h = freqz(fir_coeff, worN=8000, fs=f_s)
h = h[w <= f_select * 4]
w = w[w <= f_select * 4]

# Actual filter test
data = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
encoded = encode_data(f_s, 300, data)
signal = np.sin(2 * np.pi * f_select / f_s * np.arange(0, len(encoded))) * encoded
noise_random = np.random.normal(0, 1, len(signal))
dc_bias = 0.5
sample_data = signal + noise_random + dc_bias

filtered_data = np.convolve(sample_data, fir_coeff, mode="same")
envelope = get_envelope(filtered_data, numtaps)
decoded = envelope / np.max(envelope) > 0.5

# Plot
fig, axs = plt.subplots(2, figsize=(10, 10))
axs[0].plot(w, 20 * np.log10(abs(h)))
axs[0].set_title("Frequency response")
axs[0].set_xlabel("Frequency [Hz]")
axs[0].set_ylabel("Amplitude [dB]")
axs[0].set_xlim([0, min(f_select * 4, f_s / 2)])
axs[0].grid()

axs[1].plot(sample_data, label="Input")
axs[1].plot(filtered_data, label="Output")
axs[1].plot(encoded + 1, label="Encoded")
axs[1].plot(envelope, label="Envelope")
axs[1].plot(decoded, label="Decoded")
axs[1].set_title("Filter test")
axs[1].set_xlabel("Sample")
axs[1].set_ylabel("Amplitude")
axs[1].legend()
axs[1].grid()


plt.tight_layout()
plt.show()
