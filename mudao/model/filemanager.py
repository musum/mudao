from mudao.model.shellbase import Shell


class FileManager(Shell):
    def __init__(self, shell_type, encoder=None):
        super(FileManager, self).__init__(shell_type, encoder)
