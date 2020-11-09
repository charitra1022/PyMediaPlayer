## This file is for starting the PyMediaPlayer App and
## adding all the supported audio files from the specified directory
## If app is already running, then this file will add the songs to the
## already running instance without interfering the playback

## The media player app opened by this file is its child process
## so, make sure to terminate this file to ensure everything stops

import os
import logging
import threading
import time


## If you want to choose only a required audio extension, then remove the below import statement
## and create a 'supported_codecs' list in this file, and specify all the extensions
## The default one is from 'PyMediaPlayerAbstract.py'.
## !!!! Don't make any changes in the 'PyMediaPlayerAbstract.py'
from PyMediaPlayerAbstract import supported_codecs


## Specify your own music directory in the below 'song_path' string
## All the songs from all subdirectories will also be added!!!!.
## If your folder has a lot of songs, then it might take a longer for them to be added
## as it follows one-by-one rule for addition of songs.
song_path = 'F:\\E Drive\\Songs\\English songs'


thread_id = 1       # Keep track of the threads
def launcher(cmd):
    """Start a new terminal instance with defined command"""
    global thread_id
    logging.info("Thread %s: Starting :- %s", thread_id, cmd)
    os.system(cmd)
    logging.info("Thread %s: Finished :- %s", thread_id, cmd)
    thread_id -= 1      # remove entry once thread terminates


def main():
    date_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=date_format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : Ready for creating threads")

    for root, directories, files in os.walk(song_path):
        for file in files:
            if any(ext in file for ext in supported_codecs):
                path = root + '\\' + file
                cmd = 'python PyMediaPlayer.py "{}"'.format(path)

                thread = threading.Thread(target=launcher, args=(cmd,))
                global thread_id
                thread_id += 1      # Add the entry of active threads
                thread.start()      # Start the thread

                # Add a small time gap to prevent system crash
                # You can increase or decrease the value depending on your system
                # Smaller value means threads will be spawned at higher speed
                # If speed is very high, system may crash, or may take longer to respond
                # Recommended value for all sorts of systems is 1
                time.sleep(0.6)



if __name__ == '__main__':
    main()
