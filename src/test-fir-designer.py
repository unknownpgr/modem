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
fir_coeff, numtaps, Q = FilterDesigner.design_filter_with_numtaps(
    sample_rate, f_select, 127
)
print(f"Number of taps: {numtaps}")
print(f"Q factor: {Q}")

# Frequency response
w, h = freqz(fir_coeff, worN=8000, fs=sample_rate)
h = h[w <= f_select * 4]
w = w[w <= f_select * 4]

# Actual filter test
data = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
encoded = encode_data(sample_rate, 200, data)
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
plt.plot(w, 20 * np.log10(abs(h)))
plt.title("Frequency Response")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [dB]")
plt.savefig("graph-01-frequency-response.png")
plt.close()

plt.plot(fir_coeff)
plt.title("Filter Coefficients")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.savefig("graph-02-filter-coefficients.png")
plt.close()

t = np.linspace(0, len(sample_data) * 1000 / sample_rate, len(sample_data))
plt.plot(t, sample_data, label="Signal", color="orange", linewidth=0.5)
plt.plot(t, filtered_data, label="Filtered", color="red")
plt.plot(t, envelope, label="Envelope", color="green")
plt.plot(t, decoded - 1, label="Output", color="blue")
plt.plot(t, encoded + 1, label="Ground Truth", color="black")
plt.title("Filter Test")
plt.xlabel("Time [ms]")
plt.ylabel("Amplitude")
plt.legend()
plt.savefig("graph-03-filter-test.png")
