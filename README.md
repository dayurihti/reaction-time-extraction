**OVERVIEW**
This reaction time extraction program was initially made to help process data from the “Picture Naming Task” experiment. 
Using this program, we are able to detect human speech onset from the mass audio files. 
This program used amplitude-based measurement, detecting the 70% level of the highest amplitude. 
The cut-off was operationalized by considering the characteristic of human voice: the amplitude is consistently increasing until the peak. 
This characteristic is unique compared with the other kind of artifact noises.

**HOW IT WORKS**
In this repository, I attached a folder named "audio_all", 4 Python files, and a csv file named "rt_extraction".

**1. "audio_all" folder**
There are 32 audio files, containing human voice naming objects with a single word. I recorded my voice as a sample, feel free to use them. :)

**2. Python files**
detection.py → Defining general functions for RT detection, including the threshold, cut-offs, and flagging rules.
visualize.py →  Defining settings for the visualization of audio waveform and RT.
export.csv → Defining settings for exporting RT data into csv files.
MAIN.py → Please run this file to generate RT detection results in Terminal, show waveform from the individual audio files, and export the data into csv files.

**3. "rt.extraction" file**
The example of the RT extraction data. Feel free to check.
