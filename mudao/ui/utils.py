from PyQt5.QtWidgets import QMessageBox

from mudao.utils.logger import logger as log


class uiMixing(object):

    def __init__(self, shell, script_path=None):
        self.shell = shell
        self.cmd_path = script_path
        self.action = None
        self.webRoot = self.path = self.tmpAttr = self.os = self.sep = None
        self.mw = self.parentWidget()

    def chk_data(self, ret):
        log.debug(ret)
        data = ''
        if ret[0] != 200:
            QMessageBox.information(self, ret[1], str(ret[2]))
            return data
        try:
            data = ret[2]       # .decode(self.coder)
            log.info('Get data:\n%s' % data)
            if data == '1':
                self.mw.statusbar.showMessage('Operation finished :)')
            else:
                self.mw.statusbar.showMessage('Operation failed :(')
        except Exception as e:
            QMessageBox.information(self, 'ERR', str(e))
            log.exception(e)
        return data

    def do_action(self, *args):
        action = getattr(self.shell, self.action, None)
        if action:
            return self.chk_data(action(*args))
