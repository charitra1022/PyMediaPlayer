# This file contains all the abstract classes of PyMediaPlayer which are not directly required.
# These classes will be imported in the 'PyMediaPlayer.py' file
# NOTE:- DON'T MODIFY ANYTHING HERE, OR ELSE WHOLE CODE MIGHT GET BROKEN!!!!.


import io
import os
import platform
import tempfile

import stagger
from PIL import Image
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from PyMediaPlayerUI import Ui_PyMediaPlayer


def hhmmss(ms):
    """Converting milliseconds to hh:mm:ss format"""
    # s = 1000, m = 60000, h = 3600000
    h, r = divmod(ms, 360000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


# keep track of the Host Operating System
hostOS = platform.system().lower()
# accept only [.mp3 .wav .aac .wma .m4a .ac3 .amr .ts .flac] file extensions
supported_codecs = ['.mp3', '.wav', '.aac', '.wma', '.m4a', '.ac3', '.amr', '.ts', '.flac']
# keep track of all songs added till now to the player
songs_database = []
# supports playlist file only of this type
playlist_extension = ".pyplaylist"
# keeps track of default values of the metadata files
default_ui_values = dict()


def get_distinct_items(list1):
    """Removes duplicates from parameter,
        appends distinct only items to 'songs' list,
        returns list to be added to playlist"""

    list1 = list(set(list1))  # remove duplicates
    global songs_database
    if not songs_database:
        songs_database = list1
        return list1
    else:
        list2 = []
        for item in list1:
            if not item in songs_database:
                songs_database.append(item)
                list2.append(item)
        return list2


class PlaylistModel(QtCore.QAbstractListModel):
    """Class for Playlist Model"""

    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        try:
            if role == QtCore.Qt.DisplayRole:
                media = self.playlist.media(index.row())
                return media.canonicalUrl().fileName()
        except Exception as err:
            print("Error in PlaylistModel - data(): ", err)

    def rowCount(self, index):
        try:
            return self.playlist.mediaCount()
        except Exception as err:
            print("Error in PlaylistModel - rowCount(): ", err)


class MediaPlayer(Ui_PyMediaPlayer):
    def __init__(self):
        self.setupUi(self)
        self.setFixedSize(self.frameGeometry().width(), self.frameGeometry().height())
        try:
            self.player = QMediaPlayer()  # initializing media player object
            self.player.error.connect(self.error_alert)  # connecting the error handler
            self.player.play()  # starting it to play as soon as initialized

            self.playlist = QMediaPlaylist()  # create a playlist object
            self.player.setPlaylist(self.playlist)  # Setup the playlist.

            self.model = PlaylistModel(
                self.playlist)  # building the playlist model to let it display in the PlaylistView
            self.PlaylistView.setModel(self.model)  # setting the model to PlayListView

            # triggered when the Index of the playlist changes
            self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
            # selection model based on selection of songs from List
            selection_model = self.PlaylistView.selectionModel()
            # selection changed event trigger
            selection_model.selectionChanged.connect(self.playlist_selection_changed)

            self.player.durationChanged.connect(self.update_duration)  # when player's duration changes
            self.player.stateChanged.connect(
                self.play_pause_icon)  # when player's state changes - {Playing, Paused, Stopped}
            self.player.positionChanged.connect(self.update_position)  # when player's position changes(playing mode)
            self.player.mediaStatusChanged.connect(
                self.update_metadata_media)  # when the media is loaded into the player, it triggers
            self.TimeSlider.valueChanged.connect(self.player.setPosition)  # when TimeSlider is slided

            self.PlaylistView.doubleClicked.connect(self.remove_song)

            # button connections
            self.ShuffleButton.clicked.connect(self.shuffle_button)
            self.RepeatButton.clicked.connect(self.repeat_button)
            self.StopButton.clicked.connect(self.stop_button)
            self.PlayPauseButton.clicked.connect(self.play_button)
            self.PreviousButton.clicked.connect(self.previous_button)
            self.NextButton.clicked.connect(self.next_button)
            self.MuteButton.clicked.connect(self.mute_button)
            self.RewindButton.clicked.connect(self.rewind_button)
            self.ForwardButton.clicked.connect(self.forward_button)
            self.OpenFiles.clicked.connect(self.openfiles_button)

            self.OpenPlaylistButton.clicked.connect(self.open_playlist_button)
            self.SavePlaylistButton.clicked.connect(self.save_playlist_button)
            self.EmptyPlaylistButton.clicked.connect(self.empty_playlist_button)

            self.RewindButton.setAutoRepeat(True)  # Activate long press
            self.ForwardButton.setAutoRepeat(True)  # Activate long press
            self.RewindButton.setAutoRepeatDelay(200)  # Long press duration
            self.ForwardButton.setAutoRepeatDelay(200)  # Long press duration

            # Signal Handlers
            self.VolumeSlider.valueChanged.connect(self.volume_changed)  # when user slides volume slider

            # default value track
            default_ui_values['thumbnail'] = self.ThumbnailView.text()
            default_ui_values['time'] = self.RemainingTimeDisplay.text()
            default_ui_values['info'] = self.TitleInput.text()

            self.songDuration = 0

        except Exception as err:
            print("Error in class MediaPlayer:", err)

    def open_playlist_button(self):
        """Open local playlist file and add songs to the player playlist"""

        try:
            filter_text = "PyMediaPlayer Playlist (*{})".format(playlist_extension)

            if hostOS == 'windows': dir = os.path.expanduser('~') + "\\Documents\\PyMediaPlayer"
            if hostOS == 'linux': dir = os.path.expanduser('~') + "/Documents/PyMediaPlayer"

            if not os.path.isdir(dir): dir = ""

            file, _ = QFileDialog.getOpenFileName(self, "Open playlist file", dir, filter_text)
            if file:
                with open(file, 'r', encoding='utf-8') as playlist_file:
                    songs = playlist_file.readlines()
                    songs = ''.join(songs).split('\n')
                    self.add_songs(songs,)

        except Exception as err:
            print("Inside open_playlist_button(): ", err)

    def empty_playlist_button(self):
        """Removes all songs from the player playlist and resets it"""
        self.playlist.removeMedia(0, self.playlist.mediaCount())
        self.model.layoutChanged.emit()
        global songs_database
        songs_database = []
        self.remove_metadata_media()

    def save_playlist_button(self):
        """Save the current playlist as a local file"""

        status = self.playlist.mediaCount()
        if not status:
            alert_box = QMessageBox(self)
            alert_box.setText("Playlist is empty!")
            alert_box.setIcon(QMessageBox.Information)
            alert_box.setInformativeText("Add some songs to the playlist to save it as a file.")
            alert_box.show()
        else:
            filter_text = "PyMediaPlayer Playlist (*{})".format(playlist_extension)

            if hostOS == 'windows': dir = os.path.expanduser('~') + "\\Documents\\PyMediaPlayer"
            if hostOS == 'linux': dir = os.path.expanduser('~') + "/Documents/PyMediaPlayer"

            try: os.mkdir(dir)
            except Exception as err: pass

            name, _ = QFileDialog.getSaveFileName(self, 'Save File', dir, filter=filter_text)
            if name:
                with open(name, 'w', encoding='utf-8') as file:
                    file.write('\n'.join(songs_database))

    def add_songs(self, paths):
        """Adds songs to the current playlist from their absolute file path.
            A list of paths is passed as an argument to this function"""
        try:
            songs = []
            # accept only specific file extensions
            for path in paths:
                if any(ext in path for ext in supported_codecs): songs.append(path)

            # if any song is present, perform action
            if songs:
                songs = get_distinct_items(songs)       # only add songs which are not present

                for song in songs:
                    url = QUrl.fromLocalFile(song)
                    self.playlist.addMedia(QMediaContent(url))  # add media to the PlaylistView

                self.model.layoutChanged.emit()  # emit signal to update the PlaylistView to show up new data

                # If player is in stopped state, play the first track from new list of songs
                if self.player.state() != QMediaPlayer.PlayingState:
                    i = self.playlist.mediaCount() - len(songs)
                    self.playlist.setCurrentIndex(i)
                    self.player.play()

        except Exception as err:
            print("Error in add_songs method:", err)

    def remove_song(self, modal_index):
        """Remove the selected track if double clicked, and remove it from the 'songs' list"""
        try:
            index = modal_index.row()
            song_removed = self.playlist.media(index).canonicalUrl().toLocalFile()

            self.playlist.removeMedia(index)    # remove song from playlist
            global songs_database                        # import database into the function
            songs_database.remove(song_removed)          # remove song from the database

            self.model.layoutChanged.emit()     # update playlist view

            # if last track of the playlist is removed, play the new resulting last track
            if index == self.playlist.mediaCount() and index != 0:
                self.PlaylistView.setCurrentIndex(
                    modal_index.siblingAtRow(index - 1))  # select the new resulting last track

            if self.playlist.mediaCount() == 0: self.empty_playlist_button()

        except Exception as err:
            print("Error in MediaPlayer - remove_song(): ", err)

    def playlist_position_changed(self, i):
        """When the PlaylistView selection changes, update the player's playlist index and play the new selection"""
        try:
            if i > -1:
                ix = self.model.index(i)
                self.PlaylistView.setCurrentIndex(ix)
        except Exception as err:
            print("Error in MediaPlayer - playlist_position_changed(): ", err)

    def playlist_selection_changed(self, ix):
        """We receive a QItemSelection from selectionChanged.
        When the new item is selected in the PlaylistView"""
        try:
            i = ix.indexes()[0].row()
            self.playlist.setCurrentIndex(i)
        except Exception as err:
            print("Error in MediaPlayer - playlist_selection_changed(): ", err)

    def openfiles_button(self):
        """Adds songs from local files if not already present in the playlist"""

        filters = dict()
        if len(supported_codecs) > 1: filters['All Audio files'] = '*' + ' *'.join(supported_codecs)
        for ext in supported_codecs: filters[ext.replace('.', '').upper() + " Files"] = "*" + ext

        filter_text_list = []
        for key in filters.keys(): filter_text_list.append(key + " ({})".format(filters[key]))

        paths, _ = QFileDialog.getOpenFileNames(self, "Open file", "", ";;".join(filter_text_list))
        self.add_songs(paths,)

    def play_pause_icon(self):
        """Change the icon of the Play/Pause button based on the state of the MediaPlayer
        QMediaPlayer.StoppedState	0	Player is not palying, playback will begin from the start of the current track.
        QMediaPlayer.PlayingState	1	The media player is currently playing content.
        QMediaPlayer.PausedState	2   Player has paused playback and will resume from the position the player was paused at."""
        icon = QtGui.QIcon()
        if self.player.state() == 1:
            icon.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPauseButton.setIcon(icon)
        if self.player.state() == QMediaPlayer.StoppedState: self.TimeSlider.setEnabled(False)
        else: self.TimeSlider.setEnabled(True)

    def stop_button(self):
        self.player.stop()  # stops the player

    def play_button(self):
        """Play/Pause action based on the state of the MediaPlayer
           QMediaPlayer.StoppedState 0	Player is not palying, playback will begin from the start of the current track.
           QMediaPlayer.PlayingState 1	The media player is currently playing content.
           QMediaPlayer.PausedState	 2  Player has paused playback and will resume from the position the player was paused at."""
        if self.playlist.mediaCount():
            if self.player.state() == 0 or self.player.state() == 2:
                self.player.play()
                self.play_pause_icon()
            else:
                self.player.pause()
                self.play_pause_icon()

    def next_button(self):
        if not self.playlist.isEmpty():
            self.playlist.next()  # play next track

    def previous_button(self):
        if not self.playlist.isEmpty():
            self.playlist.previous()  # play previous track

    def mute_button(self):
        """Mute the player based on its Mute status"""
        icon = QtGui.QIcon()
        if self.player.isMuted():
            self.player.setMuted(False)
            icon.addPixmap(QtGui.QPixmap("icon/unmute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.MuteButton.setToolTip("Volume - Loud\nShortcut: Alt+M")

        else:
            self.player.setMuted(True)
            icon.addPixmap(QtGui.QPixmap("icon/mute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.MuteButton.setToolTip("Volume - Mute\nShortcut: Alt+M")
        self.MuteButton.setIcon(icon)

    def rewind_button(self):
        """Rewind the player by 2 seconds per function call"""
        value = self.TimeSlider.value()
        if value >= 2000:
            self.TimeSlider.setValue(value - 2000)  # set player -2s
        else:
            self.TimeSlider.setValue(0)  # set player at the start of the music if it has played for less than 2s

    def forward_button(self):
        """Fast Forward the player by 2 seconds per function call"""
        value = self.TimeSlider.value()
        if self.player.duration() >= self.TimeSlider.value() + 2000:
            self.TimeSlider.setValue(value + 2000)  # add 2s to the player if more than 2s of playback is left
        elif self.player.duration() > 0:
            self.TimeSlider.setValue(self.player.duration())  # if less 2s of playback is left, set player at the end
        else:
            self.TimeSlider.setValue(0)  # if there is nothing to play, set the player to 0

    def shuffle_button(self):
        """
        QMediaPlaylist.PlaybackMode.CurrentItemOnce    0- Plays a song and stops there
        QMediaPlaylist.PlaybackMode.CurrentItemInLoop  1- Plays the same song repeatedly
        QMediaPlaylist.PlaybackMode.Sequential         2- Plays all songs one by one in sequence and stops if reaches the end
        QMediaPlaylist.PlaybackMode.Loop               3- Plays from start of list if reaches the end
        QMediaPlaylist.PlaybackMode.Random             4- Plays a song randomly from the list
        """
        try:
            icon = QtGui.QIcon()
            if self.playlist.playbackMode() != QMediaPlaylist.PlaybackMode.Random:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Random)
                if self.playlist.playbackMode() == QMediaPlaylist.PlaybackMode.Random:
                    icon.addPixmap(QtGui.QPixmap("icon/shuffle-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ShuffleButton.setIcon(icon)
                    self.ShuffleButton.setToolTip("Shuffle Mode is On\nShortcut: Alt+S")
            else:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Sequential)
                if self.playlist.playbackMode() == QMediaPlaylist.PlaybackMode.Sequential:
                    icon.addPixmap(QtGui.QPixmap("icon/shuffle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ShuffleButton.setIcon(icon)
                    self.ShuffleButton.setToolTip("Shuffle Mode is Off\nShortcut: Alt+S")
                    icon.addPixmap(QtGui.QPixmap("icon/repeat-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.RepeatButton.setIcon(icon)  # reset the repeat button
                    self.RepeatButton.setToolTip("Repeat Mode - Stop if the Queue ends\nShortcut: Alt+R")
        except Exception as err:
            print("Error in MediaPlayer - shuffle_button(): ", err)

    def repeat_button(self):
        """
        QMediaPlaylist.PlaybackMode.CurrentItemOnce    0- Plays a song and stops there
        QMediaPlaylist.PlaybackMode.CurrentItemInLoop  1- Plays the same song repeatedly
        QMediaPlaylist.PlaybackMode.Sequential         2- Plays all songs one by one in sequence and stops if reaches the end
        QMediaPlaylist.PlaybackMode.Loop               3- Plays from start of list if reaches the end
        QMediaPlaylist.PlaybackMode.Random             4- Plays a song randomly from the list
        """
        try:
            icon = QtGui.QIcon()
            if self.playlist.playbackMode() == QMediaPlaylist.PlaybackMode.CurrentItemOnce:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.CurrentItemInLoop)
                self.RepeatButton.setToolTip("Repeat Mode - Repeat the same song\nShortcut: Alt+R")
                icon.addPixmap(QtGui.QPixmap("icon/repeat-one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.RepeatButton.setIcon(icon)

            elif self.playlist.playbackMode() == QMediaPlaylist.PlaybackMode.CurrentItemInLoop:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Sequential)
                self.RepeatButton.setToolTip("Repeat Mode - Stop if the Queue ends\nShortcut: Alt+R")
                icon.addPixmap(QtGui.QPixmap("icon/repeat-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.RepeatButton.setIcon(icon)

            elif self.playlist.playbackMode() == QMediaPlaylist.PlaybackMode.Sequential:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Loop)
                self.RepeatButton.setToolTip("Repeat Mode - Repeat the Queue\nShortcut: Alt+R")
                icon.addPixmap(QtGui.QPixmap("icon/repeat-queue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.RepeatButton.setIcon(icon)

            elif self.playlist.playbackMode() == QMediaPlaylist.PlaybackMode.Loop:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.CurrentItemOnce)
                self.RepeatButton.setToolTip("Repeat Mode - Play the current song and Stop there\nShortcut: Alt+R")
                icon.addPixmap(QtGui.QPixmap("icon/repeat-none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.RepeatButton.setIcon(icon)

            else:
                icon.addPixmap(QtGui.QPixmap("icon/shuffle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ShuffleButton.setIcon(icon)
                self.ShuffleButton.setToolTip("Shuffle Mode is Off\nShortcut: Alt+S")  # reset the shuffle button
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.CurrentItemOnce)
                self.RepeatButton.setToolTip("Repeat Mode - Play the current song and Stop there\nShortcut: Alt+R")
                icon.addPixmap(QtGui.QPixmap("icon/repeat-none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.RepeatButton.setIcon(icon)
        except Exception as err:
            print("Error in MediaPlayer - repeat_button(): ", err)

    def update_duration(self, duration):
        """When a media is loaded into the player, update the TimeSlider range and keep record of duration of song"""
        try:
            self.TimeSlider.setMaximum(duration)
            if duration >= 0: self.songDuration = duration
        except Exception as err:
            print("Error in MediaPlayer - update_duration(): ", err)

    def update_position(self, position):
        """Update the TimeDisplay if the TimeSlider is dragged"""
        try:
            if position >= 0: self.ElaspedTimeDisplay.setText(hhmmss(position))
            # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).

            muteStatus = self.player.isMuted()

            self.TimeSlider.blockSignals(True)
            self.player.setMuted(True)  # Mute when being dragged to prevent distortion

            self.TimeSlider.setValue(position)

            self.player.setMuted(muteStatus)  # Restore mute status when finished dragging
            self.TimeSlider.blockSignals(False)

        except Exception as err:
            print("Error in MediaPlayer - update_position(): ", err)

    def remove_metadata_media(self):
        """Remove metadata information from the UI objects"""
        self.TitleInput.setText(default_ui_values['info'])
        self.DateInput.setText(default_ui_values['info'])
        self.SampleRateInput.setText(default_ui_values['info'])
        self.ArtistInput.setText(default_ui_values['info'])
        self.DurationInput.setText(default_ui_values['info'])
        self.BitrateInput.setText(default_ui_values['info'])
        self.RemainingTimeDisplay.setText(default_ui_values['time'])
        self.ElaspedTimeDisplay.setText(default_ui_values['time'])
        self.ThumbnailView.setText(default_ui_values['thumbnail'])

    def update_metadata_media(self, e):
        """Update metadata information only when there is a media playing or paused"""
        if e == QMediaPlayer.StalledMedia or e == QMediaPlayer.BufferingMedia or e == QMediaPlayer.BufferedMedia:
            try:
                if self.player.isMetaDataAvailable():  # check if metadata is available in the current song
                    file_path = self.player.currentMedia().canonicalUrl().toLocalFile()  # get the abosulte path of the music

                    # get the absolute path of temporary folder of PyMediaPlayer
                    if hostOS == 'windows': temp_dir = str(tempfile.gettempdir()) + '\\PyMediaPlayer\\'
                    if hostOS == 'linux': temp_dir = str(tempfile.gettempdir()) + '/PyMediaPlayer/'

                    try: os.mkdir(temp_dir)  # create a temporary folder for PyMediaPlayer if not present
                    except Exception as e: pass  # generates error if already present

                    title = self.player.metaData(QMediaMetaData.Title)                 # song title
                    artist = self.player.metaData(QMediaMetaData.AlbumArtist)          # song artist
                    year = self.player.metaData(QMediaMetaData.Year)                   # song year
                    filename = self.playlist.currentMedia().canonicalUrl().fileName()  # filename of the song
                    duration = hhmmss(self.songDuration)                               # duration in hh:mm:ss style

                    bitrate = self.player.metaData(QMediaMetaData.AudioBitRate)        # song bitrate in bits/sec
                    if not bitrate: bitrate = self.player.metaData("nominal-bitrate")  # if normal method fails
                    if bitrate: bitrate //= 1000                                       # song bitrate in kilobits/sec

                    sample_rate = self.player.metaData(QMediaMetaData.SampleRate)  # song sample rate in Hz

                    # NOTE :- Everything works well in Windows OS. Linux OS or other OSes might create some bugs

                    try:
                        media = stagger.read_tag(file_path)  # read the metadata of the song
                        by_data = media[stagger.id3.APIC][0].data  # get the album art metadata
                        im = io.BytesIO(by_data)  # grab the actual format of the album art
                        imageFile = Image.open(im)  # open the image file as if it were real file
                        # temporary image file with absolute path and name
                        image_name = "{0}{1}.png".format(temp_dir,
                                                         str(self.player.currentMedia().canonicalUrl().fileName()))
                        imageFile.save(image_name)  # save the image in the desired location and name
                    except Exception as e:
                        image_name = "icon/PyMediaPlayer.png"  # if there was not album art, put Logo in its place

                    self.ThumbnailView.setScaledContents(True)  # cover the entire placeholder
                    self.ThumbnailView.setPixmap(QtGui.QPixmap(image_name))  # set the desired image as the album art

                    self.TitleInput.setText(str(title)) if title else self.TitleInput.setText(
                        str(filename))  # display title
                    self.ArtistInput.setText(str(artist)) if artist else self.ArtistInput.setText("-")  # display artist
                    self.DateInput.setText(str(year)) if year else self.DateInput.setText("-")  # display year
                    self.SampleRateInput.setText(str(sample_rate) + ' Hz') if sample_rate else self.SampleRateInput.setText(
                        "-")  # display sample rate Hz
                    self.DurationInput.setText(str(duration)) if duration else self.DurationInput.setText(
                        "-")  # display duration mm:ss
                    self.BitrateInput.setText(str(bitrate) + " kbps") if bitrate else self.BitrateInput.setText(
                        "-")  # display bitrate kbps
                    self.RemainingTimeDisplay.setText(duration)
            except Exception as err:
                print("Error in MediaPlayer - update_metadata_media(): ", err)

        else:
            self.remove_metadata_media()    # remove metadata info if player is in stopped mode

    def volume_changed(self):
        self.VolumeDisplay.setText(str(self.VolumeSlider.value()))  # display current volume
        self.player.setVolume(self.VolumeSlider.value())  # set the player volume to desired value

    def error_alert(self, *args):
        """If any error occurs in the player, this section is executed"""
        try:
            self.ThumbnailView.setPixmap(QtGui.QPixmap(""))
        except Exception as err:
            print("Error in MediaPlayer - error_alert(): ", err)
        self.ThumbnailView.setText("Seems like this media is not supported by PyMedia Player's engine!")
