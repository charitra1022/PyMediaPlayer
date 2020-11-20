# This is not an official module of PyQt5!
# It has been created purposely

# Code copied from stackoverflow.com
# Thread  :- https://stackoverflow.com/questions/8786136/pyqt-how-to-detect-and-close-ui-if-its-already-running
# Answerer:-  @ekhumoro

# Some modifications has been made based on Comments

from PyQt5 import QtWidgets, QtCore, QtNetwork
import sys


# Check if an instance is already running, and then exit if found
class SingleApplication(QtWidgets.QApplication):
    messageAvailable = QtCore.pyqtSignal(object)

    def __init__(self, argv, key):
        super().__init__(argv)
        # cleanup (only needed for unix)
        QtCore.QSharedMemory(key).attach()
        self._memory = QtCore.QSharedMemory(self)
        self._memory.setKey(key)
        if self._memory.attach():
            self._running = True
        else:
            self._running = False
            if not self._memory.create(1):
                raise RuntimeError(self._memory.errorString())

    def isRunning(self):
        return self._running


# This will help multiple instances communicate with each other
class SingleApplicationWithMessaging(SingleApplication):
    def __init__(self, argv, key):
        super().__init__(argv, key)
        self._key = key
        self._timeout = 1000

        self._server = QtNetwork.QLocalServer(self)         # server object

        if not self.isRunning():
            if not self.try_connection():
                if not self.reset_connection():
                    QtCore.qDebug("Unknown error occurred... Exiting")
                    raise RuntimeError("Unknown error occurred... Unable to start LocalServer")


    def try_connection(self):
        """Try to connect to the Local Server"""
        self._server.newConnection.connect(self.handleMessage)
        state = self._server.listen(self._key)
        if state:
            QtCore.qDebug("Server connected.")
        else:
            QtCore.qDebug("Unable to start Server.")
        return state

    def reset_connection(self):
        """Disconnect from existing server, and start a new one"""
        QtCore.qDebug("Removing server..")
        state = QtNetwork.QLocalServer.removeServer(self._key)
        if state:
            QtCore.qDebug("Remove Successful. Starting a new Server..")
            state = self.try_connection()
        else:
            QtCore.qDebug("Cannot remove server.")
        return state

    def handleMessage(self):
        """Accept the message from other instance and add it to shared memory for IPC"""
        socket = self._server.nextPendingConnection()
        if socket.waitForReadyRead(self._timeout):
            self.messageAvailable.emit(socket.readAll().data().decode('utf-8'))
            socket.disconnectFromServer()
        else:
            QtCore.qDebug(socket.errorString())

    def sendMessage(self, message):
        """Send message to already running instance"""
        if self.isRunning():
            socket = QtNetwork.QLocalSocket(self)
            socket.connectToServer(self._key, QtCore.QIODevice.WriteOnly)
            if not socket.waitForConnected(self._timeout):
                print("Inside sendMessage", socket.errorString())
                return False
            if not isinstance(message, bytes):
                message = message.encode('utf-8')
            socket.write(message)
            if not socket.waitForBytesWritten(self._timeout):
                print(socket.errorString())
                return False
            socket.disconnectFromServer()
            return True
        return False
