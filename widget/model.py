from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):
    bit32Changed = pyqtSignal(str)
    timeChanged = pyqtSignal(str)
    dateChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._bit32 = ""
        self._time = ""
        self._date = ""

    @property
    def bit32(self):
        return self._bit32

    @bit32.setter
    def bit32(self, value):
        if self._bit32 != value:
            self._bit32 = value
            self.bit32Changed.emit(value)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if self._time != value:
            self._time = value
            self.timeChanged.emit(value)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if self._date != value:
            self._date = value
            self.dateChanged.emit(value)
