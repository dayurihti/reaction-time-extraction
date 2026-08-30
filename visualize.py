import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from detection import detect_relative_threshold_and_peak

def plot_waveform(audio_path):
    result = detect_relative_threshold_and_peak(audio_path)

    rt = result["rt"]
    peak_time = result["peak_time"]
    time = np.arange(len(result["signal"])) / result["sr"]

    plt.figure(figsize=(12, 4))
    plt.plot(time, result["signal"], color="gray", alpha=0.4, label="Waveform")
    plt.plot(time, result["envelope"], color="black", linewidth=1.2, label="Envelope")
    plt.axhline(result["rt_amplitude"], color="green", linestyle=":", label="Relative Threshold")

    if rt is not None:
        plt.axvline(rt, color="blue", linestyle="--", label="RT")
    plt.axvline(peak_time, color="red", linestyle="--", label="Peak")

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.grid(True, which="major", alpha=0.6)
    ax.grid(True, which="minor", alpha=0.2)

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Peak-Validated Relative Threshold RT Detection")
    plt.legend()
    plt.tight_layout()
    plt.show()