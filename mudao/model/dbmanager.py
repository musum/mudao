import re
from mudao.model import ShellBase
from mudao.utils.tool import CONF


class DBManager(ShellBase):
    def __init__(self, **kwargs):
        super(DBManager, self).__init__(**kwargs)

    def get_data(self, connstr, action, sql=None):
        if action.upper() not in ('DBLIST', 'TABLELIST', 'COLUMNLIST', 'EXECUTESQL'):
            return None
        if self._type.lower() == 'php':
            dbtype, hst, usr, pwd, dbn = self.parse_connstr(connstr)
            key = 'DB_PHP' + dbtype.upper()
            if sql:
                pl = CONF.get(key).get(action) % (hst, usr, pwd, dbn, sql)
            else:
                pl = CONF.get(key).get(action) % (hst, usr, pwd, dbn)
        elif self._type.lower() in ('asp', 'aspx'):
            conn = self.parse_ado(connstr)
            if sql:
                pl = CONF.get('DB_' + self._type.upper() + '_ADO').get(action) % (conn, sql)
            else:
                pl = CONF.get('DB_' + self._type.upper() + '_ADO').get(action) % conn
        params = self.generate(pl)
        return self.POST(params)

    @staticmethod
    def parse_connstr(connstr):
        dbtype = re.search(r'<T>(.*)</T>', connstr).group(1)
        host = re.search(r'<H>(.*)</H>', connstr).group(1)
        user = re.search(r'<U>(.*)</U>', connstr).group(1)
        pwd = re.search(r'<P>(.*)</P>', connstr).group(1)
        dbn = re.search(r'<N>(.*)</N>', connstr).group(1)
        return dbtype, host, user, pwd, dbn

    @staticmethod
    def parse_ado(connstr):
        # dbtype = re.search(r'<T>(.*)</T>', connstr).group(1)
        conn = re.search(r'<C>(.*)</C>', connstr).group(1)
        return conn


if __name__ == "__main__":
    db = DBManager('http://localhost/test.php', 'a', 'php')
    print(db.get_data('', 'DBLIST'))
