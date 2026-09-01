This reaction time extraction program was initially made to help process data from the “Picture Naming Task” experiment. Using this program, we are able to detect human speech onset from the mass audio files. This program used amplitude-based measurement, detecting the 70% level of the highest amplitude. The cut-off was operationalized by considering the characteristic of human voice: the amplitude is consistently increasing until the peak. This characteristic is unique compared with the other kind of artifact noises.


**HOW IT WORKS**

In this repository, I attached several files and folders explained below:

**1. "audio_all" folder**

There are 32 audio files, containing human voice naming objects with a single word. I recorded my voice as a sample, feel free to use them. :)

**2. Python files**

detection.py → Defining general functions for RT detection, including the threshold, cut-offs, and flagging rules.
visualize.py →  Defining settings for the visualization of audio waveform and RT.
export.csv → Defining settings for exporting RT data into csv files.
MAIN.py → Please run this file to generate RT detection results in Terminal, show waveform from the individual audio files, and export the data into csv files.

**3. "rt.extraction" file**

The example of the RT extraction data. Feel free to check.


**This work is on Github and Google Colab!**
Github: https://github.com/dayurihti/reaction-time-extraction
Google Colab: https://colab.research.google.com/drive/1U7gjFyqGxQa02Ug9pxqz_Zb9goit2o8f?usp=sharing 
