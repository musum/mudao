import re


def parse_caidao(self, conf):
    with open(conf, 'rb') as f:
        c = f.read()
        self.conf['FLAG'] = re.match(r'<FLAG>(.*)</FLAG', c).group(1)
        self.conf['UA'] = re.match(r'<UA>(.*)</UA>', c).group(1)
        self.conf['K1'] = re.match(r'<K1>(.*)</K1>', c).group(1)
        self.conf['K2'] = re.match(r'<K2>(.*)</K2>', c).group(1)
        self.conf['PHP_BASE'] = re.match(r'<PHP_BASE>(.*)</PHP_BASE>', c)
        self.conf['ASP_BASE'] = re.match(r'<ASP_BASE>(.*)</ASP_BASE>', c)
        self.conf['ASPX_BASE'] = re.match(r'<ASPX_BASE>(.*)</ASPX_BASE>', c)
        _ = re.match(r'<GETBASEINFO>(.*)</GETBASEINFO>', c)
        self.conf['GETBASEINFO'] = {}
        self.conf['GETBASEINFO']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['GETBASEINFO']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['GETBASEINFO']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<SHOWFOLDER>(.*)</SHOWFOLDER>', c)
        self.conf['SHOWFOLDER'] = {}
        self.conf['SHOWFOLDER']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['SHOWFOLDER']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['SHOWFOLDER']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<SHOWTXTFILE>(.*)</SHOWTXTFILE>', c)
        self.conf['SHOWTXTFILE'] = {}
        self.conf['SHOWTXTFILE']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['SHOWTXTFILE']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['SHOWTXTFILE']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<SAVETXTFILE>(.*)</SAVETXTFILE>', c)
        self.conf['SAVETXTFILE'] = {}
        self.conf['SAVETXTFILE']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['SAVETXTFILE']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['SAVETXTFILE']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<DELETEFILE>(.*)</DELETEFILE>', c)
        self.conf['DELETEFILE'] = {}
        self.conf['DELETEFILE']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['DELETEFILE']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['DELETEFILE']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<DOWNFILE>(.*)</DOWNFILE>', c)
        self.conf['DOWNFILE'] = {}
        self.conf['DOWNFILE']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['DOWNFILE']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['DOWNFILE']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<UPLOADFILE>(.*)</UPLOADFILE>', c)
        self.conf['UPLOADFILE'] = {}
        self.conf['UPLOADFILE']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['UPLOADFILE']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['UPLOADFILE']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<PASTEFILE>(.*)</PASTEFILE>', c)
        self.conf['PASTEFILE'] = {}
        self.conf['PASTEFILE']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['PASTEFILE']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['PASTEFILE']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<NEWFOLDER>(.*)</NEWFOLDER>', c)
        self.conf['NEWFOLDER'] = {}
        self.conf['NEWFOLDER']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['NEWFOLDER']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['NEWFOLDER']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<WGET>(.*)</WGET>', c)
        self.conf['WGET'] = {}
        self.conf['WGET']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['WGET']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['WGET']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<SHELL>(.*)</SHELL>', c)
        self.conf['SHELL'] = {}
        self.conf['SHELL']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['SHELL']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['SHELL']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<RENAME>(.*)</RENAME>', c)
        self.conf['RENAME'] = {}
        self.conf['RENAME']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['RENAME']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['RENAME']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)
        _ = re.match(r'<SETTIME>(.*)</SETTIME>', c)
        self.conf['SETTIME'] = {}
        self.conf['SETTIME']['PHP'] = re.match(r'<PHP>(.*)</PHP>', _).group(1)
        self.conf['SETTIME']['ASP'] = re.match(r'<ASP>(.*)</ASP>', _).group(1)
        self.conf['SETTIME']['ASPX'] = re.match(r'<ASPX>(.*)</ASPX>', _).group(1)

        self.conf['DB_PHP_MYSQL_DBLIST'] = re.match(r'<DB_PHP_MYSQL_DBLIST>(.*)</DB_PHP_MYSQL_DBLIST>', c)
        self.conf['DB_PHP_MYSQL_TABLELIST'] = re.match(r'<DB_PHP_MYSQL_TABLELIST>(.*)</DB_PHP_MYSQL_TABLELIST>', c)
        self.conf['DB_PHP_MYSQL_COLUMNLIST'] = re.match(r'<DB_PHP_MYSQL_COLUMNLIST>(.*)</DB_PHP_MYSQL_COLUMNLIST>', c)
        self.conf['DB_PHP_MYSQL_EXECUTESQL'] = re.match(r'<DB_PHP_MYSQL_EXECUTESQL>(.*)</DB_PHP_MYSQL_EXECUTESQL>', c)

        self.conf['DB_PHP_POSTGRESQL_DBLIST'] = re.match(r'<DB_PHP_POSTGRESQL_DBLIST>(.*)</DB_PHP_POSTGRESQL_DBLIST>', c)
        self.conf['DB_PHP_POSTGRESQL_TABLELIST'] = re.match(r'<DB_PHP_POSTGRESQL_TABLELIST>(.*)</DB_PHP_POSTGRESQL_TABLELIST>', c)
        self.conf['DB_PHP_POSTGRESQL_COLUMNLIST'] = re.match(r'<DB_PHP_POSTGRESQL_COLUMNLIST>(.*)</DB_PHP_POSTGRESQL_COLUMNLIST>', c)
        self.conf['DB_PHP_POSTGRESQL_EXECUTESQL'] = re.match(r'<DB_PHP_POSTGRESQL_EXECUTESQL>(.*)</DB_PHP_POSTGRESQL_EXECUTESQL>', c)

        self.conf['DB_PHP_INFORMIX_DBLIST'] = re.match(r'<DB_PHP_INFORMIX_DBLIST>(.*)</DB_PHP_INFORMIX_DBLIST>', c)
        self.conf['DB_PHP_INFORMIX_TABLELIST'] = re.match(r'<DB_PHP_INFORMIX_TABLELIST>(.*)</DB_PHP_INFORMIX_TABLELIST>', c)
        self.conf['DB_PHP_INFORMIX__COLUMNLIST'] = re.match(r'<DB_PHP_INFORMIX__COLUMNLIST>(.*)</DB_PHP_INFORMIX__COLUMNLIST>', c)
        self.conf['DB_PHP_INFORMIX_EXECUTESQL'] = re.match(r'<DB_PHP_INFORMIX_EXECUTESQL>(.*)</DB_PHP_INFORMIX_EXECUTESQL>', c)

