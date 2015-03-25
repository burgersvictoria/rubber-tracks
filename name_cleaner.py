'''
*******************************************************************************************
*  Title: Rubber Tracks Name Cleaner
*  Creator: Cara Burgess
*
*  Description: Batch rename files from Converse Rubber Beats so they are sorted
*               by BPM within a directory. The format it is renaming to is
*               bpm_filename_number.    
*                 eg [..]-66_drum_loop_120.wav.wav -> 120_drum_loop_66.wav
*
*              Only works on names in the format mentioned above.
*              Currently assumes a .wav extension 
*              Current version does not support looking in subdirectories.
*
*  Directions: python ./python rubber_tracks_name_cleaner.py -s "full/directory/path"
*              where full/directory/path is the full path of the directory to
*              rename the files. 
*
*                 -h for help
*                                                                                              
*  Version History:
*     Ver: 0.1   Date: 3/24/2015   Author: Cara B.   Comment: Initial version/release
*******************************************************************************************
'''

import os

from optparse import OptionParser

def rename_files(dir_path):

   for file in os.listdir(dir_path):
      shortfilename = file.split("-")
      split_name = shortfilename[len(shortfilename)-1].split("_")
      bpm_split = split_name[len(split_name)-1]
      
      sample_num = split_name[0]
      sample_bpm_split = bpm_split.split(".")
      sample_bpm = sample_bpm_split[0]
      
      split_name.remove(split_name[0])
      split_name.remove(split_name[len(split_name)-1])
      
      new_file_name = sample_bpm + "_"
      
      for s in split_name:
         new_file_name = new_file_name + s + "_"
            
      new_file_name = new_file_name + sample_num + ".wav"
      
      os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_file_name))


def main():
   print '\n'   
   parser = OptionParser(usage="Usage: %prog -s directory",
                       version="%prog 0.1")
   parser.add_option("-s", "--source",
                   action="store_true",
                   dest="dir_to_rename",
                   default=False,
                   help="directory with the files to rename")
   (options, args) = parser.parse_args()
   dir_path = args[0]

   if len(args) != 1:
     parser.error("wrong number of arguments")

   if os.path.exists(dir_path):
      rename_files(dir_path)
   else:
      print "Please specify a valid directory"

if __name__ == '__main__':
   main()
