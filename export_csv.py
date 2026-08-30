import os
import csv

from detection import detect_relative_threshold_and_peak, flag_trial

def export_to_csv(audio_dir, output_csv):
    wav_files = sorted(
        f for f in os.listdir(audio_dir)
        if f.lower().endswith(".wav")
    )

    results = []
    for wav in wav_files:
        audio_path = os.path.join(audio_dir, wav)
        result = detect_relative_threshold_and_peak(audio_path)
        flag = flag_trial(result["rt"], result["peak_time"])

        results.append({
            "file_name": wav,
            "relative_threshold_s": result["rt"],
            "peak_time_s": result["peak_time"],
            "flag": flag
        })

    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file_name", "relative_threshold_s", "peak_time_s", "flag"]
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved {len(results)} trials to '{output_csv}'")