import os

from detection import detect_relative_threshold_and_peak, flag_trial
from visualize import plot_waveform
from export_csv import export_to_csv

# terminal settings
def print_terminal_summary(audio_dir):
    wav_files = sorted(
        f for f in os.listdir(audio_dir)
        if f.lower().endswith(".wav")
    )

# plot settings
    print("\nREACTION TIME DETECTION RESULT (Relative Threshold)\n")
    print(f"{'File Name':40s} | {'Relative Threshold (s)':>8s} | {'Peak (s)':>8s} | {'FLAG':>5s}")
    print("-" * 75)

    for wav in wav_files:
        audio_path = os.path.join(audio_dir, wav)
        result = detect_relative_threshold_and_peak(audio_path)
        flag = flag_trial(result["rt"], result["peak_time"])

        rt_str = f"{result['rt']:.4f}" if result["rt"] is not None else "NA"
        peak_str = f"{result['peak_time']:.4f}"

        print(f"{wav:40s} | {rt_str:>8s} | {peak_str:>8s} | {flag:>5s}")

## RESULT ##
if __name__ == "__main__":
    audio_dir = "audio_all"

    # print terminal
    print_terminal_summary(audio_dir)

    # export to csv
    export_to_csv(audio_dir, "rt_extraction.csv")

    # show waveform
    plot_waveform(os.path.join(audio_dir, "practice_EN_response6.wav")) # file name is adjustable