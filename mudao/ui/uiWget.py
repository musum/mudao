from PyQt5.QtWidgets import *

from mudao.ui.pannel.wget import Ui_Dialog
# from PyQt5.QtCore import pyqtSignal as Signal


class DlgWget(QDialog, Ui_Dialog):
    # sig_wget = Signal(str, str)

    def __init__(self, parent=None):
        super(DlgWget, self).__init__(parent)
        self.setupUi(self)
        # Get filepannel operation
        self.fpannel = parent
        self.btn_wget.clicked.connect(self.wget)

    def wget(self):
        # self.sig_wget.emit(self.edt_url.text(), self.edt_path.text())
        url = self.edt_url.text()
        path = self.edt_path.text()
        if url and path:
            self.fpannel.chk_data(self.fpannel.filemanager.wget(url, path))
        self.hide()
