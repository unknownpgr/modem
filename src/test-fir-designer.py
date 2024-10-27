import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import freqz

from fir_designer import FilterDesigner


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
sample_rate = 44100
f_select = 1000
q_factor = 2
fir_coeff, numtaps, Q = FilterDesigner.design_filter_with_numtaps(
    sample_rate, f_select, 127
)
print(f"Number of taps: {numtaps}")
print(f"Q factor: {Q}")
print("FIR coefficients: ")
print("[" + ",".join([str(x) for x in fir_coeff]) + "]")


# Frequency response
w, h = freqz(fir_coeff, worN=8000, fs=sample_rate)
h = h[w <= f_select * 4]
w = w[w <= f_select * 4]

# Actual filter test
data = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
encoded = encode_data(sample_rate, 300, data)
signal = (
    np.sin(2 * np.pi * f_select / sample_rate * np.arange(0, len(encoded))) * encoded
)
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
axs[0].set_xlim([0, min(f_select * 4, sample_rate / 2)])
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
