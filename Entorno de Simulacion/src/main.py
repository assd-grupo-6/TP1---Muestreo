from src.application import Application
from PyQt5 import QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Application()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()