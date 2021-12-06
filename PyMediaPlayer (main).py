## Started - 14-06-2020
## completed - 18-06-2020

#       COPYRIGHT® 2020
#       ——————————————
#       PyMediaPlayer
#       Made by "Charitra Agarwal"
#       "www.youtube.com/c/EverythingComputerized"
#       "www.linkedin.com/in/charitra1022/"


        ############               ###
   #############                  #####
  ###                            ### ###
###                             ###   ###
###                            ###     ###
###                           ###       ###
###                          ###############
###                         #################
###                         ###           ###
  ###                       ###           ###
   #############            ###           ###
       ############         ###           ###


# Instructions:-
# 1. Install libraries:- pyqt5, pyqt5-tools, stagger, pillow
# 2. Icons folder should be correctly placed


# Universal imports
import os
import sys
import tempfile
import shutil
from PyQt5.QtWidgets import QMainWindow

# Local imports
from PyMediaPlayerAbstract import MediaPlayer, hostOS
from SingleApplication import SingleApplicationWithMessaging, SingleApplication

# change the media plugin in Windows OS for better media support
# default plugin of Windows OS is 'DirectShow' released for XP which is outdated
# new plugin is 'Windows Media Foundation' released for and after Windows Vista
try:
    if hostOS == "windows":
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    # if hostOS == "linux": os.environ['QT_DEBUG_PLUGINS'] = "1"
    # enable above statement if code runs into error
    # helps in detecting the cause of error
except Exception as err:
    print("Plugin Change Error:", err)


class MainWindow(QMainWindow, MediaPlayer):
    """Setup PyMediaPlayer UI, controls and functionalities"""
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        try:
            self.setAcceptDrops(True)       # making the window accept drag and drop
            self.add_songs(sys.argv)        # add songs from command-line args
            self.show()                     # show the MainWindow as active
        except Exception as err:
            print("Error in MainWindow:", err)

    def dragEnterEvent(self, e):
        """When a drag and drop event is made onto the window"""
        try:
            if e.mimeData().hasUrls():
                e.acceptProposedAction()
        except Exception as err:
            print("Error in dragEnterEvent:", err)

    def dropEvent(self, e):
        """When the user drops the object to the Window, process and filter them, and then add them to playlist"""
        try:
            songs = []
            for url in e.mimeData().urls():
                songs.append(url.toLocalFile())     # get the absolute path of all
            self.add_songs(songs,)          # add all songs to the playlist

        except Exception as err:
            print("Error in dropEvent:", err)



    def accept_songs(self, message):
        """If another instance of app is running,
            then take the song as message and send it as a list to
            the already running instance

            NOTE:-
                Message is received as a string joined by ';'
                So, first split it into a list
                !! Make sure message is sent as a list, or else it wouldn't work"""
        try:
            message = message.split(';')
            self.add_songs(message,)
        except Exception as err:
            print("Error in accept_songs:", err)

    def closeEvent(self, e):
        """Called when user attempts to close the app.
            Redefined for Cleanup all the temporary images before leaving."""
        if hostOS == 'windows':
            temp_dir = str(tempfile.gettempdir()) + '\\PyMediaPlayer\\'
        if hostOS == 'linux':
            temp_dir = str(tempfile.gettempdir()) + '/PyMediaPlayer/'

        try:
            shutil.rmtree(temp_dir, ignore_errors=True)     # delete temporary files after closing
        except Exception as err:
            print("Error in closeEvent function:", err)


def main():
    # Unique key of the app (Shouldn't match with other apps in the Host system !!!!!)
    key = 'PYMEDIAPLAYER-PYQT5-CHARITRA-AGARWAL'

    # send commandline args as message
    if len(sys.argv) >= 1:
        app = SingleApplicationWithMessaging(sys.argv, key)
        if app.isRunning():
            print('Sending parameters to already running instance of app and Exiting.')
            app.sendMessage(';'.join(sys.argv))
    else:
        app = SingleApplication(sys.argv, key)
        if app.isRunning():
            print('Another instance of app is already running. Exiting.')

    if not app.isRunning():
        # Run the new instance if the app is not running
        window = MainWindow()                               # Main window of the app
        app.setApplicationName("PyMedia Player")            # give name of the application
        app.messageAvailable.connect(window.accept_songs)   # Connect the message passing function for IPC
        sys.exit(app.exec_())                               # Run the app

        # MainWindow is Shown from within the MainWindow class declaration


if __name__ == "__main__":
    main()
