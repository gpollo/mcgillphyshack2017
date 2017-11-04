#!/usr/bin/env python3

import sys
import subprocess

from interface import *

if __name__ == "__main__":
    subprocess.call(['sudo', 'apt-get', 'install', 'sl'])

    # create the application
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    # run the application
    window.start()
    window.show()
    app.exec_()
