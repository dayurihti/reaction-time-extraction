import numpy as np
import librosa
import os

def detect_relative_threshold_and_peak(
    audio_path,
    relative_ratio=0.7,     # RT is 70% level of the peak amplitude
    smooth_ms=5,
    min_rt=0.12,            # minimum speech onset (s)
    max_peak_gap=0.9        # maximum gap between RT and peak (s)
):
    # load audio
    signal, sr = librosa.load(audio_path, sr=None)

    print("Loaded from:", os.path.abspath(audio_path))
    print("Duration (s):", len(signal) / sr, "| Sample rate:", sr)

    # amplitude envelope
    envelope = np.abs(signal)

    win_length = max(int(sr * smooth_ms / 1000), 1)
    envelope = np.convolve(
        envelope,
        np.ones(win_length) / win_length,
        mode="same"
    )

    ## PEAK DETECTION ##
    peak_idx = np.argmax(envelope)
    peak_time = peak_idx / sr
    peak_value = envelope[peak_idx]

    relative_threshold = relative_ratio * peak_value

    # relative threshold & guard window
    crossing_indices = np.where(envelope >= relative_threshold)[0]

    rt_time = None
    for idx in crossing_indices:
        t = idx / sr

        if t < min_rt:                      # minimum speech onset
            continue
        if t > peak_time:                   # RT must happened before peak
            break
        if (peak_time - t) > max_peak_gap:  # RT - peak gap checking
            continue

        rt_time = t
        break

    # return dict
    return {
        "signal": signal,
        "envelope": envelope,
        "sr": sr,
        "rt": rt_time,
        "peak_time": peak_time,
        "rt_amplitude": relative_threshold
    }

## FLAGGING ##
def flag_trial(rt, peak_time):
    if rt is None:
        return "HARD_FLAG"
    if rt < 0.10 or rt > 2.10:
        return "HARD_FLAG"
    if rt < 0.20:
        return "SOFT_FLAG"
    if (peak_time - rt) > 0.9:
        return "SOFT_FLAG"
    return "-"