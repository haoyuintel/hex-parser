from PyQt5.QtCore import QRegExp, pyqtSlot
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, \
    QPushButton, QSpacerItem, QSizePolicy
import pyperclip

from utils.watcher_utils import watch_parse_channel
from utils.parse_utils import parse_32_bit_t
from widget.model import Model


class WidgetLayout(QWidget):

    label_width = 100
    input_width = 200

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data_model = Model()
        self.set_wathcer()
        self.set_validators()
        self.set_style()

    def set_wathcer(self):
        self.bit32_input.textChanged.connect(self.on_text_changed)
        self.data_model.dateChanged.connect(self.date_parse_input.setText)
        self.data_model.timeChanged.connect(self.time_parse_input.setText)
        self.date_button.clicked.connect(self.copy)
        self.time_button.clicked.connect(self.copy)

    def set_validators(self):
        bit32_regex = QRegExp(r'^[0-9a-fA-F]{0,8}$')
        # bit32_regex = QRegExp(r'^[0-1]{0,32}$')
        bit32_validator = QRegExpValidator(bit32_regex, self)
        self.bit32_input.setValidator(bit32_validator)

    @pyqtSlot(str)
    def on_text_changed(self, text):
        res = watch_parse_channel(text, parse_32_bit_t)
        if res is not None:
            self.data_model.date = res[0]
            self.data_model.time = res[1]
            print(self.data_model.time)
            print(self.data_model.date)

    def copy(self):
        if self.sender() == self.time_button:
            pyperclip.copy(self.data_model.time)
        else:
            pyperclip.copy(self.data_model.date)

    def initUI(self):
        main_layout = QVBoxLayout()

        bit32_layout = QHBoxLayout()
        bit32_label = QLabel("32bit(hex): ")
        bit32_label.setFixedWidth(self.label_width)
        self.bit32_input = QLineEdit()
        self.bit32_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        bit32_layout.addWidget(bit32_label)
        bit32_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        bit32_layout.addWidget(self.bit32_input)
        main_layout.addLayout(bit32_layout)

        date_parse_layout = QHBoxLayout()
        date_parse_label = QLabel("DATE PARSE: ")
        date_parse_label.setFixedWidth(self.label_width)
        self.date_parse_input = QLineEdit()
        self.date_parse_input.setReadOnly(True)
        self.date_parse_input.setFixedWidth(self.input_width)
        self.date_button = QPushButton("COPY")
        date_parse_layout.addWidget(date_parse_label)
        date_parse_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        date_parse_layout.addWidget(self.date_parse_input)
        date_parse_layout.addWidget(self.date_button)
        main_layout.addLayout(date_parse_layout)

        time_parse_layout = QHBoxLayout()
        time_parse_label = QLabel("TIME PARSE: ")
        time_parse_label.setFixedWidth(self.label_width)
        self.time_parse_input = QLineEdit()
        self.time_parse_input.setReadOnly(True)
        self.time_parse_input.setFixedWidth(self.input_width)
        self.time_button = QPushButton("COPY")
        time_parse_layout.addWidget(time_parse_label)
        time_parse_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        time_parse_layout.addWidget(self.time_parse_input)
        time_parse_layout.addWidget(self.time_button)
        main_layout.addLayout(time_parse_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("32bit hex parser")
        self.setFixedSize(500, 300)

        self.show()

    def set_style(self):
        self.setStyleSheet(
            """
            QWidget {
                font-size: 20px;
            }
            
            QPushButton {
                font-size: 20px;
            }
            
            QLabel {
                font-size: 20px;
            }
            """
        )