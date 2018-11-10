import re
from configparser import ConfigParser

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QMessageBox

from mudao.utils.logger import logger as log


def parse_caidao(conf):
    ret = {}
    with open(conf, 'rb') as f:
        c = f.read().decode('utf-16')
        #print(c)
        ret['FLAG'] = re.search(r'<FLAG>(.*)</FLAG>', c).group(1)
        ret['UA'] = re.search(r'<UA>(.*)</UA>', c).group(1)
        ret['K1'] = re.search(r'<K1>(.*)</K1>', c).group(1)
        ret['K2'] = re.search(r'<K2>(.*)</K2>', c).group(1)
        ret['PHP_BASE'] = re.search(r'<PHP_BASE>(.*)</PHP_BASE>', c, re.DOTALL).group(1).strip()
        ret['ASP_BASE'] = re.search(r'<ASP_BASE>(.*)</ASP_BASE>', c, re.DOTALL).group(1).strip()
        ret['ASPX_BASE'] = re.search(r'<ASPX_BASE>(.*)</ASPX_BASE>', c, re.DOTALL).group(1).strip()
        _ = re.search(r'<GETBASEINFO>(.*)</GETBASEINFO>', c, re.DOTALL).group(1).strip()
        ret['GETBASEINFO'] = {}
        ret['GETBASEINFO']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['GETBASEINFO']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['GETBASEINFO']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<SHOWFOLDER>(.*)</SHOWFOLDER>', c, re.DOTALL).group(1).strip()
        ret['SHOWFOLDER'] = {}
        ret['SHOWFOLDER']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['SHOWFOLDER']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['SHOWFOLDER']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<SHOWTXTFILE>(.*)</SHOWTXTFILE>', c, re.DOTALL).group(1).strip()
        ret['SHOWTXTFILE'] = {}
        ret['SHOWTXTFILE']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['SHOWTXTFILE']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['SHOWTXTFILE']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<SAVETXTFILE>(.*)</SAVETXTFILE>', c, re.DOTALL).group(1).strip()
        ret['SAVETXTFILE'] = {}
        ret['SAVETXTFILE']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['SAVETXTFILE']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['SAVETXTFILE']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<DELETEFILE>(.*)</DELETEFILE>', c, re.DOTALL).group(1).strip()
        ret['DELETEFILE'] = {}
        ret['DELETEFILE']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['DELETEFILE']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['DELETEFILE']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<DOWNFILE>(.*)</DOWNFILE>', c, re.DOTALL).group(1).strip()
        ret['DOWNFILE'] = {}
        ret['DOWNFILE']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['DOWNFILE']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['DOWNFILE']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<UPLOADFILE>(.*)</UPLOADFILE>', c, re.DOTALL).group(1).strip()
        ret['UPLOADFILE'] = {}
        ret['UPLOADFILE']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['UPLOADFILE']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['UPLOADFILE']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<PASTEFILE>(.*)</PASTEFILE>', c, re.DOTALL).group(1).strip()
        ret['PASTEFILE'] = {}
        ret['PASTEFILE']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['PASTEFILE']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['PASTEFILE']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<NEWFOLDER>(.*)</NEWFOLDER>', c, re.DOTALL).group(1).strip()
        ret['NEWFOLDER'] = {}
        ret['NEWFOLDER']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['NEWFOLDER']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['NEWFOLDER']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<WGET>(.*)</WGET>', c, re.DOTALL).group(1).strip()
        ret['WGET'] = {}
        ret['WGET']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['WGET']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['WGET']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<SHELL>(.*)</SHELL>', c, re.DOTALL).group(1).strip()
        ret['SHELL'] = {}
        ret['SHELL']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['SHELL']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['SHELL']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<RENAME>(.*)</RENAME>', c, re.DOTALL).group(1).strip()
        ret['RENAME'] = {}
        ret['RENAME']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['RENAME']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['RENAME']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()
        _ = re.search(r'<SETTIME>(.*)</SETTIME>', c, re.DOTALL).group(1).strip()
        ret['SETTIME'] = {}
        ret['SETTIME']['PHP'] = re.search(r'<PHP>(.*)</PHP>', _, re.DOTALL).group(1).strip()
        ret['SETTIME']['ASP'] = re.search(r'<ASP>(.*)</ASP>', _, re.DOTALL).group(1).strip()
        ret['SETTIME']['ASPX'] = re.search(r'<ASPX>(.*)</ASPX>', _, re.DOTALL).group(1).strip()

        ret['DB_PHP_MYSQL_DBLIST'] = re.search(r'<DB_PHP_MYSQL_DBLIST>(.*)</DB_PHP_MYSQL_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_MYSQL_TABLELIST'] = re.search(r'<DB_PHP_MYSQL_TABLELIST>(.*)</DB_PHP_MYSQL_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_MYSQL_COLUMNLIST'] = re.search(r'<DB_PHP_MYSQL_COLUMNLIST>(.*)</DB_PHP_MYSQL_COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_MYSQL_EXECUTESQL'] = re.search(r'<DB_PHP_MYSQL_EXECUTESQL>(.*)</DB_PHP_MYSQL_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        ret['DB_PHP_POSTGRESQL_DBLIST'] = re.search(r'<DB_PHP_POSTGRESQL_DBLIST>(.*)</DB_PHP_POSTGRESQL_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_POSTGRESQL_TABLELIST'] = re.search(r'<DB_PHP_POSTGRESQL_TABLELIST>(.*)</DB_PHP_POSTGRESQL_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_POSTGRESQL_COLUMNLIST'] = re.search(r'<DB_PHP_POSTGRESQL_COLUMNLIST>(.*)</DB_PHP_POSTGRESQL_COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_POSTGRESQL_EXECUTESQL'] = re.search(r'<DB_PHP_POSTGRESQL_EXECUTESQL>(.*)</DB_PHP_POSTGRESQL_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        ret['DB_PHP_INFORMIX_DBLIST'] = re.search(r'<DB_PHP_INFORMIX_DBLIST>(.*)</DB_PHP_INFORMIX_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_INFORMIX_TABLELIST'] = re.search(r'<DB_PHP_INFORMIX_TABLELIST>(.*)</DB_PHP_INFORMIX_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_INFORMIX__COLUMNLIST'] = re.search(r'<DB_PHP_INFORMIX__COLUMNLIST>(.*)</DB_PHP_INFORMIX__COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_INFORMIX_EXECUTESQL'] = re.search(r'<DB_PHP_INFORMIX_EXECUTESQL>(.*)</DB_PHP_INFORMIX_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        ret['DB_PHP_ORACLE_DBLIST'] = re.search(r'<DB_PHP_ORACLE_DBLIST>(.*)</DB_PHP_ORACLE_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_ORACLE_TABLELIST'] = re.search(r'<DB_PHP_ORACLE_TABLELIST>(.*)</DB_PHP_ORACLE_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_ORACLE_COLUMNLIST'] = re.search(r'<DB_PHP_ORACLE_COLUMNLIST>(.*)</DB_PHP_ORACLE_COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_ORACLE_EXECUTESQL'] = re.search(r'<DB_PHP_ORACLE_EXECUTESQL>(.*)</DB_PHP_ORACLE_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        ret['DB_PHP_MSSQL_DBLIST'] = re.search(r'<DB_PHP_MSSQL_DBLIST>(.*)</DB_PHP_MSSQL_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_MSSQL_TABLELIST'] = re.search(r'<DB_PHP_MSSQL_TABLELIST>(.*)</DB_PHP_MSSQL_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_MSSQL_COLUMNLIST'] = re.search(r'<DB_PHP_MSSQL_COLUMNLIST>(.*)</DB_PHP_MSSQL_COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_PHP_MSSQL_EXECUTESQL'] = re.search(r'<DB_PHP_MSSQL_EXECUTESQL>(.*)</DB_PHP_MSSQL_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        ret['DB_ASP_ADO_DBLIST'] = re.search(r'<DB_ASP_ADO_DBLIST>(.*)</DB_ASP_ADO_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_ASP_ADO_TABLELIST'] = re.search(r'<DB_ASP_ADO_TABLELIST>(.*)</DB_ASP_ADO_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_ASP_ADO_COLUMNLIST'] = re.search(r'<DB_ASP_ADO_COLUMNLIST>(.*)</DB_ASP_ADO_COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_ASP_ADO_EXECUTESQL'] = re.search(r'<DB_ASP_ADO_EXECUTESQL>(.*)</DB_ASP_ADO_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        ret['DB_ASPX_ADO_DBLIST'] = re.search(r'<DB_ASPX_ADO_DBLIST>(.*)</DB_ASPX_ADO_DBLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_ASPX_ADO_TABLELIST'] = re.search(r'<DB_ASPX_ADO_TABLELIST>(.*)</DB_ASPX_ADO_TABLELIST>', c, re.DOTALL).group(1).strip()
        ret['DB_ASPX_ADO_COLUMNLIST'] = re.search(r'<DB_ASPX_ADO_COLUMNLIST>(.*)</DB_ASPX_ADO_COLUMNLIST>', c, re.DOTALL).group(1).strip()
        ret['DB_ASPX_ADO_EXECUTESQL'] = re.search(r'<DB_ASPX_ADO_EXECUTESQL>(.*)</DB_ASPX_ADO_EXECUTESQL>', c, re.DOTALL).group(1).strip()

        return ret


CONF = parse_caidao('../config/caidao.conf')


def parse(nn, base, dot=2):
    n = nn / base
    m = nn % base
    return '.'.join((str(n), str(m)[:dot]))


def human_size(num, dot=2):
    base = {'B': 1, 'K': 1024, 'M': 1048576, 'G': 1073741824, 'T': 1099511627776, 'P': 1125899906842624}
    if num >= base['M']:
        if num < base['G']:
            return parse(num, base['M'], dot) + ' M'
        elif num < base['T']:
            return parse(num, base['G'], dot) + ' G'
        elif num < base['P']:
            return parse(num, base['T'], dot) + ' T'
        else:
            return parse(num, base['P'], dot) + ' P'
    elif num < base['K']:
        return parse(num, base['B'], dot) + ' B'
    else:
        return parse(num, base['K'], dot) + ' K'


def parse_result(html, flag):
    pat = re.compile(r'%s(.*?)%s' % (flag, flag), re.DOTALL)
    ret = pat.findall(html)
    if ret:
        return ret[0]
    return ''


# def add_item(data, root):
#     NEW = True
#     item = None
#     name = data[0] if isinstance(data, (tuple, list)) else str(data)
#
#     if isinstance(root, QTreeWidget):
#         for i in range(root.topLevelItemCount()):
#             if name == root.topLevelItem(i).text(0):
#                 item = root.topLevelItem(i)
#                 NEW = False
#                 break
#         if NEW:
#             item = make_item(data, 'disk')
#             root.addTopLevelItem(item)
#         item.setExpanded(True)
#     elif isinstance(root, QTreeWidgetItem):
#         for i in range(root.childCount()):
#             if name == root.child(i).text(0):
#                 item = root.child(i)
#                 NEW = False
#                 break
#         if NEW:
#             item = make_item(data)
#             root.addChild(item)
#         item.setExpanded(True)
#     return item


def make_item(it, icon=None):
    if not icon and isinstance(it, (tuple, list)):
        if it[0].endswith('/'):
            icon = 'folder'
        elif '.' in it[0]:
            icon = 'file'
        else:
            icon = 'binary'

    if icon in ('database', 'table', 'column'):
        icon_path = './images/db_icons/%s.png' % icon
    elif icon in ('disk', 'folder', 'file', 'binary', 'image', 'jpg'):
        icon_path = './images/file_icons/%s_24px.png' % icon
    else:
        icon_path = './images/default.png'

    item = QTreeWidgetItem()
    if isinstance(it, (tuple, list)):
        for k, v in enumerate(it):
            v = v[:-1] if v.endswith('/') else v
            item.setText(k, v)
    else:
        it = str(it)
        it = it[:-1] if it.endswith('/') else it
        item.setText(0, it)
    item.setIcon(0, QIcon(icon_path))

    return item


def chk_data(ret, msg_widget=None):
    log.debug(ret)
    data = ''
    if ret[0] != 200:
        QMessageBox.information(None, ret[1], str(ret[2]))
        return data
    try:
        data = ret[2]       # .decode(self.coder)
        log.info('Get data:\n%s' % data)
        if not msg_widget:
            return data
        if data == '-1':
            msg_widget.showMessage('Operation failed :(')
        else:
            msg_widget.showMessage('Operation finished :)')
        return data
    except Exception as e:
        QMessageBox.information(None, 'ERR', str(e))
        log.exception(e)


class Config(ConfigParser):
    def __init__(self, conf=None):
        self.conf = conf

    def save(self, path=None):
        path = path or self.conf
        with open(path, 'w') as f:
            self.write(f)

    def load(self, path=None):
        path = path or self.conf
        try:
            self.read(path, encoding='utf-8')
        except IOError:
            print('File not existed')


if __name__ == "__main__":
    conf = '../config/caidao.conf'
    _ = parse_caidao(conf)
    for k, v in _.items():
        print('%s: %s' % (k, v))

    # Config().save('mudao.ini')
    # c = Config('../config/conf.ini').load()
    # print(c.sections())
