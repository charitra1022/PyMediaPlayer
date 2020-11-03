from PyQt5 import QtWidgets, QtGui, QtCore


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

