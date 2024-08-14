from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QDoubleSpinBox, QLineEdit, QVBoxLayout, \
    QPushButton, QSpacerItem, QSizePolicy
from utils.watcher_utils import on_text_changed


class WidgetLayout(QWidget):

    label_width = 100
    input_width = 200

    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_wathcer()
        self.set_validators()

    def set_wathcer(self):
        self.bit32_input.textChanged.connect(on_text_changed)

    def set_validators(self):
        bit32_regex = QRegExp(r'^[0-9a-fA-F]{0,32}$')
        bit32_validator = QRegExpValidator(bit32_regex, self)
        self.bit32_input.setValidator(bit32_validator)


    def initUI(self):
        main_layout = QVBoxLayout()

        bit32_layout = QHBoxLayout()
        bit32_label = QLabel("32bit: ")
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
        self.date_parse_input.setFixedWidth(self.input_width)
        date_button = QPushButton("COPY")
        date_parse_layout.addWidget(date_parse_label)
        date_parse_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        date_parse_layout.addWidget(self.date_parse_input)
        date_parse_layout.addWidget(date_button)
        main_layout.addLayout(date_parse_layout)

        time_parse_layout = QHBoxLayout()
        time_parse_label = QLabel("TIME PARSE: ")
        time_parse_label.setFixedWidth(self.label_width)
        self.time_parse_input = QLineEdit()
        self.time_parse_input.setFixedWidth(self.input_width)
        time_button = QPushButton("COPY")
        time_parse_layout.addWidget(time_parse_label)
        time_parse_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        time_parse_layout.addWidget(self.time_parse_input)
        time_parse_layout.addWidget(time_button)
        main_layout.addLayout(time_parse_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("32bit hex parser")
        self.setFixedSize(450, 300)

        self.show()
