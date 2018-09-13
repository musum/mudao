# -*- coding: utf-8 -*-
import os
import sys
from subprocess import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool, QProcess, Qt
from PyQt5.QtWidgets import *

from mudao.ui import *
from mudao.utils.config import Config
from mudao.utils.logger import logger
# from utils import XStream


def main(*args, **kwargs):
    app = QApplication(*args)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
