import os
import numpy as np
import librosa
import csv

def detect_relative_threshold_and_peak(
    audio_path,
    relative_ratio=0.7,
    smooth_ms=5
):
    signal, sr = librosa.load(audio_path, sr=None)

    envelope = np.abs(signal)

    win_length = int(sr * smooth_ms / 1000)
    win_length = max(win_length, 1)
    envelope = np.convolve(
        envelope,
        np.ones(win_length) / win_length,
        mode="same"
    )

    peak_idx = np.argmax(envelope)
    peak_time = peak_idx / sr
    peak_value = envelope[peak_idx]

    relative_threshold = relative_ratio * peak_value

    crossing_indices = np.where(envelope >= relative_threshold)[0]
    relative_cross_time = (
        crossing_indices[0] / sr
        if len(crossing_indices) > 0
        else None
    )
def detect_relative_threshold_and_peak(
    audio_path,
    relative_ratio=0.7,
    smooth_ms=5,
    min_rt=0.12,      # speech onset guard (s)
    max_peak_gap=0.9  # max allowed peak - RT gap (s)
):
    signal, sr = librosa.load(audio_path, sr=None)

    envelope = np.abs(signal)

    win_length = int(sr * smooth_ms / 1000)
    win_length = max(win_length, 1)
    envelope = np.convolve(
        envelope,
        np.ones(win_length) / win_length,
        mode="same"
    )

    # === PEAK DETECTION ===
    peak_idx = np.argmax(envelope)
    peak_time = peak_idx / sr
    peak_value = envelope[peak_idx]

    relative_threshold = relative_ratio * peak_value

    ## RELATIVE THRESHOLD WITH GUARD WINDOW ##
    crossing_indices = np.where(envelope >= relative_threshold)[0]

    relative_cross_time = None
    for idx in crossing_indices:
        t = idx / sr

        # speech onset guard
        if t < min_rt:
            continue

        # peak validation (RT must precede peak)
        if t > peak_time:
            break

        # peak-gap sanity check
        if (peak_time - t) > max_peak_gap:
            continue

        relative_cross_time = t
        break

    return relative_cross_time, peak_time

def flag_trial(rt, peak_time):
    if rt is None:
        return "HARD_FLAG" # RT tidak terdeteksi
    if rt < 0.10 or rt > 2.10:
        return "HARD_FLAG"
    if rt < 0.20:
        return "SOFT_FLAG"
    if (peak_time - rt) > 0.9:
        return "SOFT_FLAG"
    return "-"

import csv
import os

if __name__ == "__main__":

    audio_dir = "audio_all"
    output_csv = "rt_extraction.csv"

    wav_files = sorted(
        f for f in os.listdir(audio_dir)
        if f.lower().endswith(".wav")
    )

    results = []

    for wav in wav_files:
        audio_path = os.path.join(audio_dir, wav)

        rt, peak = detect_relative_threshold_and_peak(audio_path)
        flag = flag_trial(rt, peak)

        results.append({
            "file_name": wav,
            "relative_threshold_s": rt,
            "peak_time_s": peak,
            "flag": flag
        })

    ## WRITE TO CSV ##
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "file_name",
                "relative_threshold_s",
                "peak_time_s",
                "flag"
            ]
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved {len(results)} trials to '{output_csv}'")
