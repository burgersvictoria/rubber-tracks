# rubber-tracks

Scripts I've written in relation to the Converse Rubber Tracks Sample Library project. 
For now just a simple batch rename was needed.

----------name_cleaner.py-----------

Input a directory containing rubber tracks samples to rename all samples to format bpm_name_num.wav for easier sorting by bpm.

Batch rename files from Converse Rubber Beats so they are sorted by BPM within a directory. The format it is renaming to is
bpm_filename_number.    

eg [..]-66_drum_loop_120.wav.wav -> 120_drum_loop_66.wav

Only works on names in the format mentioned above
Currently assumes a .wav extension 
Current version does not support looking in subdirectories