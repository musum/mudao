import re
from mudao.model import ShellBase
from mudao.utils.tool import CONF


class DBManager(ShellBase):
    def __init__(self, **kwargs):
        super(DBManager, self).__init__(**kwargs)

    def database(self, connstr):
        if self.type.lower() == 'php':
            dbtype, hst, usr, pwd, dbn, dbl, dbp = self.parse_connstr(connstr)
            key = '_'.join(('DB_PHP', dbtype.upper(), 'DBLIST'))
            if dbtype.upper() == 'MYSQL':
                dbn = dbn or 'mysql'
                dbl = dbl or 'utf-8'
                pl = CONF.get(key) % (hst, usr, pwd, dbn, dbl)
            elif dbtype.upper() == 'MSSQL':
                pl = CONF.get(key) % (hst, usr, pwd, dbn)
            elif dbtype.upper() in ('INFORMIX', 'ORACLE'):
                pl = CONF.get(key) % (hst, usr, pwd)
            elif dbtype.upper() == 'POSTGRESQL':
                pl = CONF.get(key) % (hst, usr, pwd, dbn, dbp)

        elif self.type.lower() in ('asp', 'aspx'):
            conn = self.parse_ado(connstr)
            pl = CONF.get('DB_' + self.type.upper() + '_ADO_DBLIST') % conn
        params = self.generate(pl)
        return self.POST(params)

    def tables(self, connstr, database=None):
        if self.type.lower() == 'php':
            dbtype, hst, usr, pwd, dbn, dbl, dbp = self.parse_connstr(connstr)
            key = '_'.join(('DB_PHP', dbtype.upper(), 'TABLELIST'))
            if dbtype.upper() == 'MYSQL':
                dbn = database or dbn or 'mysql'
                dbl = dbl or 'utf-8'
                pl = CONF.get(key) % (hst, usr, pwd, dbn, dbl)
            elif dbtype.upper() == 'MSSQL':
                pl = CONF.get(key) % (hst, usr, pwd, dbn)
            elif dbtype.upper() in ('INFORMIX', 'ORACLE'):
                pl = CONF.get(key) % (hst, usr, pwd, database)
            elif dbtype.upper() == 'POSTGRESQL':
                pl = CONF.get(key) % (hst, usr, pwd, dbn, dbp)

        elif self.type.lower() in ('asp', 'aspx'):
            conn = self.parse_ado(connstr)
            pl = CONF.get('DB_' + self.type.upper() + '_ADO_TABLELIST') % conn
        params = self.generate(pl)
        return self.POST(params)

    def columns(self, connstr, table, database=None):
        if self.type.lower() == 'php':
            dbtype, hst, usr, pwd, dbn, dbl, dbp = self.parse_connstr(connstr)
            key = '_'.join(('DB_PHP', dbtype.upper(), 'COLUMNLIST'))
            if dbtype.upper() == 'MYSQL':
                dbn = database or dbn or 'mysql'
                dbl = dbl or 'utf-8'
                pl = CONF.get(key) % (hst, usr, pwd, dbn, table, dbl)
            elif dbtype.upper() == 'MSSQL':
                pl = CONF.get(key) % (hst, usr, pwd, dbn, table)
            elif dbtype.upper() in ('INFORMIX', 'ORACLE'):
                pl = CONF.get(key) % (hst, usr, pwd, table)
            elif dbtype.upper() == 'POSTGRESQL':
                pl = CONF.get(key) % (hst, usr, pwd, dbn, dbp, table)

        elif self.type.lower() in ('asp', 'aspx'):
            conn = self.parse_ado(connstr)
            pl = CONF.get('DB_' + self.type.upper() + '_ADO_COLUMNLIST') % (conn, table)
        params = self.generate(pl)
        return self.POST(params)

    def execute(self, connstr, sql, database=None):
        if self.type.lower() == 'php':
            dbtype, hst, usr, pwd, dbn, dbl, dbp = self.parse_connstr(connstr)
            key = '_'.join(('DB_PHP', dbtype.upper(), 'EXECUTESQL'))
            if dbtype.upper() == 'MYSQL':
                dbn = database or dbn or 'mysql'
                dbl = dbl or 'utf-8'
                pl = CONF.get(key) % (hst, usr, pwd, dbn, sql, dbl)
            elif dbtype.upper() in ('MSSQL', 'ORACLE'):
                dbn = database or dbn
                pl = CONF.get(key) % (hst, usr, pwd, dbn, sql)
            elif dbtype.upper() == 'INFORMIX':
                pl = CONF.get(key) % (hst, usr, pwd, sql)
            elif dbtype.upper() == 'POSTGRESQL':
                dbn = database or dbn
                pl = CONF.get(key) % (hst, usr, pwd, dbn, dbp, sql)

        elif self.type.lower() in ('asp', 'aspx'):
            conn = self.parse_ado(connstr)
            pl = CONF.get('DB_' + self.type.upper() + '_ADO_EXECUTESQL') % (conn, sql)
        params = self.generate(pl)
        return self.POST(params)
    #
    # def get_data(self, connstr, action, sql=None):
    #     if action.upper() not in ('DBLIST', 'TABLELIST', 'COLUMNLIST', 'EXECUTESQL'):
    #         return None
    #     if self.type.lower() == 'php':
    #         dbtype, hst, usr, pwd, dbn, dbl, dbp = self.parse_connstr(connstr)
    #         key = '_'.join(('DB_PHP', dbtype.upper(), action.upper()))
    #         if sql:
    #             if not dbp:
    #                 pl = CONF.get(key) % (hst, usr, pwd, dbn, sql, dbl)
    #             else:
    #                 pl = CONF.get(key) % (hst, usr, pwd, dbn, dbp, sql)
    #         else:
    #             if not dbp:
    #                 pl = CONF.get(key) % (hst, usr, pwd, dbn, dbl)
    #             else:
    #                 pl = CONF.get(key) % (hst, usr, pwd, dbn, dbp)
    #     elif self.type.lower() in ('asp', 'aspx'):
    #         conn = self.parse_ado(connstr)
    #         if sql:
    #             pl = CONF.get('DB_' + self.type.upper() + '_ADO').get(action) % (conn, sql)
    #         else:
    #             pl = CONF.get('DB_' + self.type.upper() + '_ADO').get(action) % conn
    #     params = self.generate(pl)
    #     return self.POST(params)

    @staticmethod
    def parse_connstr(connstr):
        dbtype = re.search(r'<T>(.*)</T>', connstr).group(1)
        host = re.search(r'<H>(.*)</H>', connstr).group(1)
        dbp = re.search(r'<PORT>(.*)</PORT>', connstr).group(1) if re.search(r'<PORT>(.*)</PORT>', connstr) else None
        user = re.search(r'<U>(.*)</U>', connstr).group(1)
        pwd = re.search(r'<P>(.*)</P>', connstr).group(1)
        dbn = re.search(r'<N>(.*)</N>', connstr).group(1) if re.search(r'<N>(.*)</N>', connstr) else None
        dbl = re.search(r'<L>(.*)</L>', connstr).group(1) if re.search(r'<L>(.*)</L>', connstr) else None
        return dbtype, host, user, pwd, dbn, dbl, dbp

    @staticmethod
    def parse_ado(connstr):
        dbtype = re.search(r'<T>(.*)</T>', connstr).group(1)
        if dbtype == 'ADO':
            conn = re.search(r'<C>(.*)</C>', connstr).group(1)
        elif dbtype == 'XDB':
            conn = re.search(r'<X>(.*)</X>', connstr).group(1)
        return conn


if __name__ == "__main__":
    db = DBManager('http://localhost/test.php', 'a', 'php')
    print(db.get_data('', 'DBLIST'))
