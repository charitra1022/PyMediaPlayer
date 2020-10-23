## Started - 14-06-2020
## completed - 18-06-2020

#       COPYRIGHT® 2020
#       ——————————————
#       PyMediaPlayer
#       Made by "Charitra Agarwal"
#       "www.youtube.com/c/EverythingComputerized"
#       "www.linkedin.com/in/chiku1022/"


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


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QAbstractListModel
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import Qt
from PIL import Image, ImageQt
import stagger, io, os, tempfile, sys

# change the media plugin in Windows OS for better media support
# default plugin of Windows OS is 'DirectShow' released for XP which is outdated
# new plugin is 'Windows Media Foundation' released for and after Windows Vista
try:
    import platform
    if platform.system().lower() == "windows": os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
except Exception as e:
    print("Plugin Change Error:", e)


def hhmmss(ms):
    # s = 1000, m = 60000, h = 3600000
    h, r = divmod(ms, 360000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class Ui_PyMediaPlayer(object):
    def setupUi(self, PyMediaPlayer):
        PyMediaPlayer.setObjectName("PyMediaPlayer")
        PyMediaPlayer.setFixedSize(630, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PyMediaPlayer.sizePolicy().hasHeightForWidth())
        PyMediaPlayer.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/PyMediaPlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PyMediaPlayer.setWindowIcon(icon)
        PyMediaPlayer.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(PyMediaPlayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 9, 618, 451))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayoutFullApp = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayoutFullApp.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutFullApp.setObjectName("verticalLayoutFullApp")
        self.horizontalLayoutUpper = QtWidgets.QHBoxLayout()
        self.horizontalLayoutUpper.setObjectName("horizontalLayoutUpper")
        self.ThumbnailView = QtWidgets.QLabel(self.layoutWidget)
        self.ThumbnailView.setMaximumSize(QtCore.QSize(360, 360))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(16)
        self.ThumbnailView.setFont(font)
        self.ThumbnailView.setStyleSheet("background:rgba(12,12,233,0.02);\n"
                                         "color:rgba(0,0,0,0.2);\n"
                                         "border:none;\n"
                                         "opacity:0.1;")
        self.ThumbnailView.setTextFormat(QtCore.Qt.RichText)
        self.ThumbnailView.setScaledContents(True)
        self.ThumbnailView.setAlignment(QtCore.Qt.AlignCenter)
        self.ThumbnailView.setWordWrap(True)
        self.ThumbnailView.setObjectName("ThumbnailView")
        self.horizontalLayoutUpper.addWidget(self.ThumbnailView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # playlist
        self.PlaylistView = QtWidgets.QListView(self.layoutWidget)
        self.PlaylistView.setMaximumSize(QtCore.QSize(240, 360))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PlaylistView.setFont(font)
        self.PlaylistView.setAcceptDrops(True)
        self.PlaylistView.setStyleSheet("QListView{\n"
                                        "background-color:rgba(12,12,233,0.02);\n"
                                        "border:none;\n"
                                        "}\n"
                                        "QToolTip { \n"
                                        "background-color: white; \n"
                                        "color:rgba(0,0,0,0.9); \n"
                                        " border: black solid 1px\n"
                                        " }")
        self.PlaylistView.setProperty("showDropIndicator", True)
        self.PlaylistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.PlaylistView.setAlternatingRowColors(True)
        self.PlaylistView.setUniformItemSizes(True)
        self.PlaylistView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.PlaylistView.setObjectName("PlaylistView")

        self.verticalLayout.addWidget(self.PlaylistView)
        self.horizontalLayoutMetadata = QtWidgets.QHBoxLayout()
        self.horizontalLayoutMetadata.setObjectName("horizontalLayoutMetadata")
        self.verticalLayoutMetadataLabel = QtWidgets.QVBoxLayout()
        self.verticalLayoutMetadataLabel.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayoutMetadataLabel.setObjectName("verticalLayoutMetadataLabel")
        self.TitleLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayoutMetadataLabel.addWidget(self.TitleLabel)
        self.ArtistLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArtistLabel.sizePolicy().hasHeightForWidth())
        self.ArtistLabel.setSizePolicy(sizePolicy)
        self.ArtistLabel.setObjectName("ArtistLabel")
        self.verticalLayoutMetadataLabel.addWidget(self.ArtistLabel)
        self.DateLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateLabel.sizePolicy().hasHeightForWidth())
        self.DateLabel.setSizePolicy(sizePolicy)
        self.DateLabel.setObjectName("DateLabel")
        self.verticalLayoutMetadataLabel.addWidget(self.DateLabel)
        self.SampleRateLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SampleRateLabel.sizePolicy().hasHeightForWidth())
        self.SampleRateLabel.setSizePolicy(sizePolicy)
        self.SampleRateLabel.setObjectName("SampleRateLabel")
        self.verticalLayoutMetadataLabel.addWidget(self.SampleRateLabel)
        self.DurationLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DurationLabel.sizePolicy().hasHeightForWidth())
        self.DurationLabel.setSizePolicy(sizePolicy)
        self.DurationLabel.setObjectName("DurationLabel")
        self.verticalLayoutMetadataLabel.addWidget(self.DurationLabel)
        self.BitrateLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BitrateLabel.sizePolicy().hasHeightForWidth())
        self.BitrateLabel.setSizePolicy(sizePolicy)
        self.BitrateLabel.setObjectName("BitrateLabel")
        self.verticalLayoutMetadataLabel.addWidget(self.BitrateLabel)
        self.horizontalLayoutMetadata.addLayout(self.verticalLayoutMetadataLabel)
        self.verticalLayoutMetadataInput = QtWidgets.QVBoxLayout()
        self.verticalLayoutMetadataInput.setObjectName("verticalLayoutMetadataInput")

        self.TitleInput = QtWidgets.QLabel(self.layoutWidget)
        self.TitleInput.setObjectName("TitleInput")
        self.TitleInput.setMaximumSize(QtCore.QSize(185, 100))
        self.verticalLayoutMetadataInput.addWidget(self.TitleInput)
        self.ArtistInput = QtWidgets.QLabel(self.layoutWidget)
        self.ArtistInput.setText("")
        self.ArtistInput.setObjectName("ArtistInput")
        self.ArtistInput.setMaximumSize(QtCore.QSize(185, 100))
        self.verticalLayoutMetadataInput.addWidget(self.ArtistInput)
        self.DateInput = QtWidgets.QLabel(self.layoutWidget)
        self.DateInput.setText("")
        self.DateInput.setObjectName("DateInput")
        self.DateInput.setMaximumSize(QtCore.QSize(185, 100))
        self.verticalLayoutMetadataInput.addWidget(self.DateInput)
        self.SampleRateInput = QtWidgets.QLabel(self.layoutWidget)
        self.SampleRateInput.setText("")
        self.SampleRateInput.setObjectName("SampleRateInput")
        self.verticalLayoutMetadataInput.addWidget(self.SampleRateInput)
        self.DurationInput = QtWidgets.QLabel(self.layoutWidget)
        self.DurationInput.setText("")
        self.DurationInput.setObjectName("DurationInput")
        self.verticalLayoutMetadataInput.addWidget(self.DurationInput)
        self.BitrateInput = QtWidgets.QLabel(self.layoutWidget)
        self.BitrateInput.setText("")
        self.BitrateInput.setObjectName("BitrateInput")
        self.verticalLayoutMetadataInput.addWidget(self.BitrateInput)
        self.horizontalLayoutMetadata.addLayout(self.verticalLayoutMetadataInput)
        self.verticalLayout.addLayout(self.horizontalLayoutMetadata)
        self.horizontalLayoutUpper.addLayout(self.verticalLayout)

        self.verticalLayoutFullApp.addLayout(self.horizontalLayoutUpper)
        self.verticalLayoutBottomPanel = QtWidgets.QVBoxLayout()
        self.verticalLayoutBottomPanel.setObjectName("verticalLayoutBottomPanel")
        self.horizontalLayoutTimePanel = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTimePanel.setObjectName("horizontalLayoutTimePanel")
        self.ElaspedTimeDisplay = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.ElaspedTimeDisplay.setFont(font)
        self.ElaspedTimeDisplay.setMinimumSize(QtCore.QSize(27, 0))
        self.ElaspedTimeDisplay.setMaximumSize(QtCore.QSize(27, 16777215))
        self.ElaspedTimeDisplay.setObjectName("ElaspedTimeDisplay")
        self.horizontalLayoutTimePanel.addWidget(self.ElaspedTimeDisplay)
        self.TimeSlider = QtWidgets.QSlider(self.layoutWidget)
        self.TimeSlider.setStyleSheet("QSlider::groove:horizontal {\n"
                                      "background: white;\n"
                                      "height: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::sub-page:horizontal {\n"
                                      "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
                                      "    stop: 0 #66e, stop: 1 #bbf);\n"
                                      "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
                                      "    stop: 0 #bbf, stop: 1 #55f);\n"
                                      "height: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::add-page:horizontal {\n"
                                      "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
                                      "     stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                      "height: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:horizontal {\n"
                                      "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                      "    stop:0 #52307c, stop: 1 #ece6ff);\n"
                                      "width: 13px;\n"
                                      "margin-top: -2px;\n"
                                      "margin-bottom: -2px;\n"
                                      "border-radius: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                      "    stop:0 #bca0dc, stop:1 #e0d6ff);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::sub-page:horizontal:disabled {\n"
                                      "background: #bbb;\n"
                                      "border-color: #999;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::add-page:horizontal:disabled {\n"
                                      "background: #eee;\n"
                                      "border-color: #999;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:horizontal:disabled {\n"
                                      "background: #eee;\n"
                                      "border: 1px solid #aaa;\n"
                                      "border-radius: 4px;\n"
                                      "}")
        self.TimeSlider.setSliderPosition(0)
        self.TimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TimeSlider.setObjectName("TimeSlider")
        self.horizontalLayoutTimePanel.addWidget(self.TimeSlider)
        self.RemainingTimeDisplay = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.RemainingTimeDisplay.setMinimumSize(QtCore.QSize(27, 0))
        self.RemainingTimeDisplay.setMaximumSize(QtCore.QSize(27, 16777215))
        self.RemainingTimeDisplay.setFont(font)
        self.RemainingTimeDisplay.setObjectName("RemainingTimeDisplay")
        self.horizontalLayoutTimePanel.addWidget(self.RemainingTimeDisplay)
        self.verticalLayoutBottomPanel.addLayout(self.horizontalLayoutTimePanel)
        self.horizontalLayoutControls = QtWidgets.QHBoxLayout()
        self.horizontalLayoutControls.setObjectName("horizontalLayoutControls")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ShuffleButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShuffleButton.sizePolicy().hasHeightForWidth())
        self.ShuffleButton.setSizePolicy(sizePolicy)
        self.ShuffleButton.setStyleSheet("QPushButton{\n"
                                         "color: #333;\n"
                                         "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                         "width: 30px; \n"
                                         "height: 30px;\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                         "}\n"
                                         "")
        self.ShuffleButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/shuffle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShuffleButton.setIcon(icon1)
        self.ShuffleButton.setIconSize(QtCore.QSize(21, 21))
        self.ShuffleButton.setObjectName("ShuffleButton")
        self.horizontalLayout_2.addWidget(self.ShuffleButton)
        self.RepeatButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepeatButton.sizePolicy().hasHeightForWidth())
        self.RepeatButton.setSizePolicy(sizePolicy)
        self.RepeatButton.setStyleSheet("QPushButton{\n"
                                        "color: #333;\n"
                                        "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                        "width: 30px; \n"
                                        "height: 30px;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                        "}\n"
                                        "")
        self.RepeatButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/repeat-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RepeatButton.setIcon(icon2)
        self.RepeatButton.setIconSize(QtCore.QSize(21, 21))
        self.RepeatButton.setObjectName("RepeatButton")
        self.horizontalLayout_2.addWidget(self.RepeatButton)
        self.StopButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setStyleSheet("QPushButton{\n"
                                      "color: #333;\n"
                                      "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                      "width: 30px; \n"
                                      "height: 30px;\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                      "}\n"
                                      "")
        self.StopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopButton.setIcon(icon3)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout_2.addWidget(self.StopButton)
        self.horizontalLayoutControls.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutControls.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PreviousButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreviousButton.sizePolicy().hasHeightForWidth())
        self.PreviousButton.setSizePolicy(sizePolicy)
        self.PreviousButton.setStyleSheet("QPushButton{\n"
                                          "color: #333;\n"
                                          "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                          "width: 30px; \n"
                                          "height: 30px;\n"
                                          "border-radius: 15px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed{\n"
                                          "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                          "}\n"
                                          "")
        self.PreviousButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviousButton.setIcon(icon4)
        self.PreviousButton.setObjectName("PreviousButton")
        self.horizontalLayout.addWidget(self.PreviousButton)
        self.RewindButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RewindButton.sizePolicy().hasHeightForWidth())
        self.RewindButton.setSizePolicy(sizePolicy)
        self.RewindButton.setStyleSheet("QPushButton{\n"
                                        "color: #333;\n"
                                        "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                        "width: 30px; \n"
                                        "height: 30px;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                        "}\n"
                                        "")
        self.RewindButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/rewind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RewindButton.setIcon(icon5)
        self.RewindButton.setObjectName("RewindButton")
        self.horizontalLayout.addWidget(self.RewindButton)
        self.PlayPauseButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayPauseButton.sizePolicy().hasHeightForWidth())
        self.PlayPauseButton.setSizePolicy(sizePolicy)
        self.PlayPauseButton.setStyleSheet("QPushButton{\n"
                                           "color: #333;\n"
                                           "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                           "width: 40px; \n"
                                           "height: 40px;\n"
                                           "border-radius: 15px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                           "}\n"
                                           "")
        self.PlayPauseButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPauseButton.setIcon(icon6)
        self.PlayPauseButton.setIconSize(QtCore.QSize(25, 25))
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        self.horizontalLayout.addWidget(self.PlayPauseButton)
        self.ForwardButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ForwardButton.sizePolicy().hasHeightForWidth())
        self.ForwardButton.setSizePolicy(sizePolicy)
        self.ForwardButton.setStyleSheet("QPushButton{\n"
                                         "color: #333;\n"
                                         "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                         "width: 30px; \n"
                                         "height: 30px;\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                         "}\n"
                                         "")
        self.ForwardButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ForwardButton.setIcon(icon7)
        self.ForwardButton.setObjectName("ForwardButton")
        self.horizontalLayout.addWidget(self.ForwardButton)
        self.NextButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy)
        self.NextButton.setStyleSheet("QPushButton{\n"
                                      "color: #333;\n"
                                      "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                      "width: 30px; \n"
                                      "height: 30px;\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                      "}\n"
                                      "")
        self.NextButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextButton.setIcon(icon8)
        self.NextButton.setObjectName("NextButton")
        self.horizontalLayout.addWidget(self.NextButton)
        self.horizontalLayoutControls.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutControls.addItem(spacerItem2)
        self.VolumeSlider = QtWidgets.QSlider(self.layoutWidget)
        self.VolumeSlider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "border: 1px solid #bbb;\n"
                                        "background: white;\n"
                                        "height: 7px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::sub-page:horizontal {\n"
                                        "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
                                        "    stop: 0 #66e, stop: 1 #bbf);\n"
                                        "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
                                        "    stop: 0 #bbf, stop: 1 #55f);\n"
                                        "border: 0px solid #777;\n"
                                        "height: 10px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal {\n"
                                        "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
                                        "     stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                        "\n"
                                        "border: 0px solid #777;\n"
                                        "height: 10px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                        "    stop:0 #52307c, stop: 1 #ece6ff);\n"
                                        "width: 13px;\n"
                                        "margin-top: -5px;\n"
                                        "margin-bottom: -5px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal:hover {\n"
                                        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                        "    stop:0 #bca0dc, stop:1 #e0d6ff);\n"
                                        "border: 0px solid #444;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::sub-page:horizontal:disabled {\n"
                                        "background: #bbb;\n"
                                        "border-color: #999;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal:disabled {\n"
                                        "background: #eee;\n"
                                        "border-color: #999;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal:disabled {\n"
                                        "background: #eee;\n"
                                        "border: 1px solid #aaa;\n"
                                        "border-radius: 4px;\n"
                                        "}")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setPageStep(10)
        self.VolumeSlider.setSliderPosition(100)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayoutControls.addWidget(self.VolumeSlider)
        self.MuteButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MuteButton.sizePolicy().hasHeightForWidth())
        self.MuteButton.setSizePolicy(sizePolicy)
        self.MuteButton.setStyleSheet("QPushButton{\n"
                                      "color: #333;\n"
                                      "background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
                                      "width: 25px; \n"
                                      "height: 25px;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
                                      "}\n"
                                      "")
        self.MuteButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/unmute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MuteButton.setIcon(icon9)
        self.MuteButton.setIconSize(QtCore.QSize(25, 25))
        self.MuteButton.setObjectName("MuteButton")
        self.horizontalLayoutControls.addWidget(self.MuteButton)
        self.VolumeDisplay = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.VolumeDisplay.setFont(font)
        self.VolumeDisplay.setMinimumSize(QtCore.QSize(20, 0))
        self.VolumeDisplay.setMaximumSize(QtCore.QSize(20, 16777215))
        self.VolumeDisplay.setObjectName("VolumeDisplay")
        self.horizontalLayoutControls.addWidget(self.VolumeDisplay)
        spacerItem3 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutControls.addItem(spacerItem3)
        self.verticalLayoutBottomPanel.addLayout(self.horizontalLayoutControls)
        self.verticalLayoutFullApp.addLayout(self.verticalLayoutBottomPanel)
        PyMediaPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyMediaPlayer)
        QtCore.QMetaObject.connectSlotsByName(PyMediaPlayer)

    def retranslateUi(self, PyMediaPlayer):
        _translate = QtCore.QCoreApplication.translate
        PyMediaPlayer.setWindowTitle(_translate("PyMediaPlayer", "PyMedia Player"))
        self.ThumbnailView.setText(
            _translate("PyMediaPlayer", "Drag and Drop songs here to add them to the Playlist."))
        self.PlaylistView.setToolTip(_translate("PyMediaPlayer", "Playlist - Drag and drop songs here to play them"))
        self.ElaspedTimeDisplay.setText(_translate("PyMediaPlayer", "--:--"))
        self.TimeSlider.setToolTip(_translate("PyMediaPlayer", "Track Seek"))
        self.RemainingTimeDisplay.setText(_translate("PyMediaPlayer", "--:--"))
        self.ShuffleButton.setToolTip(_translate("PyMediaPlayer", "Shuffle Mode is Off\nShortcut: Alt+S"))
        self.RepeatButton.setToolTip(
            _translate("PyMediaPlayer", "Repeat Mode - Stop if the Queue ends\nShortcut: Alt+R"))
        self.StopButton.setToolTip(_translate("PyMediaPlayer", "Stop\nShortcut: Alt+X"))
        self.PreviousButton.setToolTip(_translate("PyMediaPlayer", "Previous Track\nShortcut: Alt+P"))
        self.RewindButton.setToolTip(_translate("PyMediaPlayer", "-2s/Long press to Rewind\nShortcut: Ctrl+Alt+P"))
        self.PlayPauseButton.setToolTip(_translate("PyMediaPlayer", "Play/Pause\nShortcut: Spacebar"))
        self.ForwardButton.setToolTip(
            _translate("PyMediaPlayer", "+2s/Long press to Fast Forward\nShortcut: Ctrl+Alt+N"))
        self.NextButton.setToolTip(_translate("PyMediaPlayer", "Next Track\nShortcut: Alt+N"))
        self.VolumeSlider.setToolTip(_translate("PyMediaPlayer", "Volume Selector"))
        self.MuteButton.setToolTip(_translate("PyMediaPlayer", "Volume - Loud\nShortcut: Alt+M"))
        self.VolumeDisplay.setText(_translate("PyMediaPlayer", "100"))
        self.TitleLabel.setText(_translate("PyMediaPlayer", "Title:"))
        self.ArtistLabel.setText(_translate("PyMediaPlayer", "Artist:"))
        self.DateLabel.setText(_translate("PyMediaPlayer", "Year:"))
        self.SampleRateLabel.setText(_translate("PyMediaPlayer", "Sample:"))
        self.DurationLabel.setText(_translate("PyMediaPlayer", "Duration:"))
        self.BitrateLabel.setText(_translate("PyMediaPlayer", "Bitrate:"))

        self.ShuffleButton.setShortcut(_translate("PyMediaPlayer", "Alt+S"))
        self.MuteButton.setShortcut(_translate("PyMediaPlayer", "Alt+M"))
        self.RepeatButton.setShortcut(_translate("PyMediaPlayer", "Alt+R"))
        self.StopButton.setShortcut(_translate("PyMediaPlayer", "Alt+X"))
        self.PreviousButton.setShortcut(_translate("PyMediaPlayer", "Alt+P"))
        self.RewindButton.setShortcut(_translate("PyMediaPlayer", "Ctrl+Alt+P"))
        self.PlayPauseButton.setShortcut(_translate("PyMediaPlayer", "Space"))
        self.ForwardButton.setShortcut(_translate("PyMediaPlayer", "Ctrl+Alt+N"))
        self.NextButton.setShortcut(_translate("PyMediaPlayer", "Alt+N"))



#############################################################################################
class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                media = self.playlist.media(index.row())
                return media.canonicalUrl().fileName()
        except Exception as e: pass

    def rowCount(self, index):
        try: return self.playlist.mediaCount()
        except Exception as e: pass


class MainWindow(QMainWindow, Ui_PyMediaPlayer):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        try:
            self.player = QMediaPlayer()                # initializing media player object
            self.player.error.connect(self.erroralert)  # connecting the error handler
            self.player.play()                          # starting it to play as soon as initialized

            self.playlist = QMediaPlaylist()            # create a playlist object
            self.player.setPlaylist(self.playlist)      # Setup the playlist.

            self.model = PlaylistModel(self.playlist)   # building the playlist model to let it display in the PlaylistView
            self.PlaylistView.setModel(self.model)      # setting the model to PlayListView

            self.playlist.currentIndexChanged.connect(self.playlist_position_changed)   # triggered when the Index of the playlist changes
            selection_model = self.PlaylistView.selectionModel()                        # selection model based on selection of songs from List
            selection_model.selectionChanged.connect(self.playlist_selection_changed)

            self.player.durationChanged.connect(self.update_duration)       # when player's duration changes
            self.player.stateChanged.connect(self.play_pause_icon)          # when player's state changes - {PLaying, Paused, Stopped}
            self.player.positionChanged.connect(self.update_position)       # when player's position changes(playing mode)
            self.player.mediaStatusChanged.connect(self.metadata_media)     # when the media is loaded into the player, it triggers
            self.TimeSlider.valueChanged.connect(self.player.setPosition)   # when TimeSlider is slided

            self.setAcceptDrops(True)                                       # making the window accept drag and drop

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

            self.RewindButton.setAutoRepeat(True)       # Activate long press
            self.ForwardButton.setAutoRepeat(True)      # Activate long press
            self.RewindButton.setAutoRepeatDelay(200)   # Long press duration
            self.ForwardButton.setAutoRepeatDelay(200)  # Long press duration

            # Signal Handlers
            self.VolumeSlider.valueChanged.connect(self.volume_changed)     # when user slides volume slider

            self.show()                                                     # show the MainWindow as active
        except Exception as e: pass

    def play_pause_icon(self):
        """Change the icon of the Play/Pause button based on the state of the MediaPlayer
        QMediaPlayer.StoppedState	0	Player is not palying, playback will begin from the start of the current track.
        QMediaPlayer.PlayingState	1	The media player is currently playing content.
        QMediaPlayer.PausedState	2   Player has paused playback and will resume from the position the player was paused at."""
        icon = QtGui.QIcon()
        if self.player.state() == 1: icon.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else: icon.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPauseButton.setIcon(icon)

    def volume_changed(self):
        self.VolumeDisplay.setText(str(self.VolumeSlider.value()))  # display current volume
        self.player.setVolume(self.VolumeSlider.value())            # set the player volume to desired value

    def stop_button(self):
        self.player.stop()  # stops the player

    def play_button(self):
        """Play/Pause action based on the state of the MediaPlayer
           QMediaPlayer.StoppedState	0	Player is not palying, playback will begin from the start of the current track.
           QMediaPlayer.PlayingState	1	The media player is currently playing content.
           QMediaPlayer.PausedState	2   Player has paused playback and will resume from the position the player was paused at."""
        if self.player.state() == 0 or self.player.state() == 2:
            self.player.play()
            self.play_pause_icon()
        else:
            self.player.pause()
            self.play_pause_icon()

    def next_button(self):
        self.playlist.next()        # play next track

    def previous_button(self):
        self.playlist.previous()    # play previous track

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
        if value >= 2000: self.TimeSlider.setValue(value - 2000)  # set player -2s
        else: self.TimeSlider.setValue(0)                         # set player at the start of the music if it has played for less than 2s

    def forward_button(self):
        """Fast Forward the player by 2 seconds per function call"""
        value = self.TimeSlider.value()
        if self.player.duration() >= self.TimeSlider.value() + 2000:
            self.TimeSlider.setValue(value + 2000)              # add 2s to the player if more than 2s of playback is left
        elif self.player.duration() > 0:
            self.TimeSlider.setValue(self.player.duration())    # if less 2s of playback is left, set player at the end
        else:
            self.TimeSlider.setValue(0)                         # if there is nothing to play, set the player to 0


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
        except Exception as e: pass


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
        except Exception as e: pass


    def dragEnterEvent(self, e):
        """When a drag and drop event is made onto the window"""
        try:
            if e.mimeData().hasUrls(): e.acceptProposedAction()
        except Exception as e: pass


    def dropEvent(self, e):
        """When the user drops the object to the Window, process and filter them, and then add them to playlist"""
        try:
            for url in e.mimeData().urls():
                # accept only [.mp3 .wav .aac .wma .m4a .ac3 .amr .ts .flac] file extensions
                supported_codecs = ['.mp3', '.wav', '.aac', '.wma', '.m4a', '.ac3', '.amr', '.ts', '.flac']
                if any(ext in url.fileName() for ext in supported_codecs):
                    self.playlist.addMedia(QMediaContent(url))  # add media to the PlaylistView

            self.model.layoutChanged.emit()  # emit signal to update the PlaylistView to show up new data

            # If player is in stopped state, play the first track
            if self.player.state() != QMediaPlayer.PlayingState:
                i = self.playlist.mediaCount() - len(e.mimeData().urls())
                self.playlist.setCurrentIndex(i)
                self.player.play()
        except Exception as e: pass


    '''def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "mp3 Audio (*.mp3);")
        if path:
            self.playlist.addMedia(
                QMediaContent(QUrl.fromLocalFile(path)))
        self.model.layoutChanged.emit()'''


    def update_duration(self, duration):
        """When a media is loaded into tthe player, update the TimeSlider range and TimeDisplay"""
        try:
            self.TimeSlider.setMaximum(duration)
            if duration >= 0: self.RemainingTimeDisplay.setText(hhmmss(duration))
        except Exception as e: pass


    def update_position(self, position):
        """Update the TimeDisplay if the TimeSlider is dragged"""
        try:
            if position >= 0: self.ElaspedTimeDisplay.setText(hhmmss(position))
            # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
            self.TimeSlider.blockSignals(True)
            self.TimeSlider.setValue(position)
            self.TimeSlider.blockSignals(False)
        except Exception as e: pass


    def playlist_selection_changed(self, ix):
        """We receive a QItemSelection from selectionChanged.
        When the new item is selected in the PlaylistView"""
        try:
            i = ix.indexes()[0].row()
            self.playlist.setCurrentIndex(i)
        except Exception as e: pass


    def playlist_position_changed(self, i):
        """When the PlaylistView selection changes, update the player's playlist index and play the new selection"""
        try:
            if i > -1:
                ix = self.model.index(i)
                self.PlaylistView.setCurrentIndex(ix)
        except Exception as e: pass


    def erroralert(self, *args):
        """If any error occurs in the player, this section is executed"""
        try: self.ThumbnailView.setPixmap(QtGui.QPixmap(""))
        except Exception as e: pass
        self.ThumbnailView.setText("Seems like this media is not supported by PyMedia Player's engine!")


    def metadata_media(self):
        try:
            if self.player.isMetaDataAvailable():                   # check if metadata is available in the current song
                file_path = self.player.currentMedia().canonicalUrl().toLocalFile()     # get the abosulte path of the music
                temp_dir = str(tempfile.gettempdir()) + '\\PyMediaPlayer\\'             # get the absolute path of temporary folder of PyMediaPlayer

                try: os.mkdir(temp_dir)          # create a temporary folder for PyMediaPlayer if not present
                except Exception as e: pass      # generates error if already present

                title = self.player.metaData(QMediaMetaData.Title)                      # song title
                artist = self.player.metaData(QMediaMetaData.AlbumArtist)               # song artist
                year = self.player.metaData(QMediaMetaData.Year)                        # song year
                duration = hhmmss(self.player.metaData(QMediaMetaData.Duration))        # song duration/length in mm:ss
                bitrate = self.player.metaData(QMediaMetaData.AudioBitRate) // 1000     # song bitrate in kbps
                sample_rate = self.player.metaData(QMediaMetaData.SampleRate)           # song sample rate in Hz

                try:
                    media = stagger.read_tag(file_path)                                                                    # read the metadata of the song
                    by_data = media[stagger.id3.APIC][0].data                                                              # get the album art metadata
                    im = io.BytesIO(by_data)                                                                               # grab the actual format of the album art
                    imageFile = Image.open(im)                                                                             # open the image file as if it were real file
                    image_name = "{0}{1}.png".format(temp_dir, str(self.player.currentMedia().canonicalUrl().fileName()))  # temporary image file with absolute path and name
                    imageFile.save(image_name)                                                                             # save the image in the desired location and name
                except Exception as e: image_name = "icon/PyMediaPlayer.png"                    # if there was not album art, put Logo in its place

                self.ThumbnailView.setScaledContents(True)                                      # cover the entire placeholder
                self.ThumbnailView.setPixmap(QtGui.QPixmap(image_name))                         # set the desired image as the album art
                self.TitleInput.setText(str(title)) if title else self.TitleInput.setText("-")                                 # display title
                self.ArtistInput.setText(str(artist)) if artist else self.ArtistInput.setText("-")                             # display artist
                self.DateInput.setText(str(year)) if year else self.DateInput.setText("-")                                     # display year
                self.DurationInput.setText(str(duration)) if duration else self.DurationInput.setText("-")                     # display duration mm:ss
                self.BitrateInput.setText(str(bitrate) + " kbps") if bitrate else self.BitrateInput.setText("-")               # display bitrate kbps
                self.SampleRateInput.setText(str(sample_rate) + " Hz") if sample_rate else self.SampleRateInput.setText("-")   # display sample rate Hz

        except Exception as e: pass


    def closeEvent(self, event):
        temp_dir = str(tempfile.gettempdir()) + '\\PyMediaPlayer\\'
        try:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)     # delete temporary files after closing
        except Exception as e: print("Error in closeEvent fuction:", e)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("PyMedia Player")
    window = MainWindow()
    sys.exit(app.exec_())
    # MainWindow is Shown from within the MainWindow class declaration


if __name__ == "__main__": main()

