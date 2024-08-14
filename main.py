import sys

from PyQt5.QtWidgets import QApplication

from parser_widgetLayout import WidgetLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = WidgetLayout()

    sys.exit(app.exec_())