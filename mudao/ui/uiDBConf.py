from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal as Signal
from mudao.ui.pannel.dbconfig import Ui_Dialog


PHP_PG = '''\
<T>POSTGRESQL</T>
<H>localhost</H>
<PORT>5432</PORT>
<U>postgres</U>
<P>dbpwd</P>
<N>postgres</N>
'''

PHP_INF = '''\
<T>INFORMIX</T>
<H>localhost</H>
<U>dbuser</U>
<P>dbpwd</P>
'''

PHP_ORA = '''\
<T>ORACLE</T>
<H>localhost</H>
<U>dbuser</U>
<P>dbpwd</P>
'''

PHP_MS = '''\
<T>MSSQL</T>
<H>localhost</H>
<U>sa</U>
<P></P>
<N>master</N>
'''

PHP_MY = '''\
<T>MYSQL</T>
<H>localhost</H>
<U>root</U>
<P></P>
<N>mysql</N>
'''

PHP_MY_OPT = '''\
<T>MYSQL</T>
<H>localhost</H>
<U>root</U>
<P></P>
<O>act=login</O>
'''

PHP_MY_LO = '''\
<T>MYSQL</T>
<H>localhost</H>
<U>root</U>
<P></P>
<L>utf8</L>
'''

ADO_SQLSERVER = '''\
<T>ADO</T>
<C>Driver={Sql Server};Server=(local);Database=master;Uid=sa;Pwd=</C>
'''

ADO_OLEDB = '''\
<T>ADO</T>
<C>Provider=SQLOLEDB.1;User ID=sa;Password=;Initial Catalog=master;Data Source=(local);</C>
'''

ADO_OLEDB1 = '''\
<T>ADO</T>
<C>Provider=SQLOLEDB.1;Initial Catalog=master;Data Source=(local);Integrated Security=SSPI;</C>
'''

ADO_MY = '''\
<T>ADO</T>
<C>Driver={MySQL};Server=localhost;database=mysql;UID=root;PWD=</C>
'''

ADO_OLEDB4 = '''\
<T>ADO</T>
<C>Provider=Microsoft.Jet.OLEDB.4.0;Data Source=c:\test.mdb</C>
'''

ADO_ACCESS = '''\
<T>ADO</T>
<C>Driver={Microsoft Access Driver(*.mdb)};DBQ=c:\test.mdb</C>
'''

ADO_ORA = '''\
<T>ADO</T>
<C>Provider=OraOLEDB.Oracle;Data Source=test;User Id=sys;Password=;Persist Security Info=True;</C>
'''

ADO_DNS = '''\
<T>ADO</T>
<C>Dsn=DsnName;</C>
'''

ADO_DEFAULT = '''\
<T>ADO</T>
<C>Driver={Sql Server};Server=(local);Database=master;Uid=sa;Pwd=123456</C>
'''

XDB_SQLSERVER = '''\
<T>XDB</T>
<X>Data Source=.;Initial Catalog=master;Persist Security Info=True;User Id=sa;Pwd=</X>
'''

XDB_JDBC_ORA = '''\
<T>XDB</T>
<X>
oracle.jdbc.driver.OracleDriver
jdbc:oracle:thin:user/password@127.0.0.1:1521/test
</X>
'''

XDB_JDBC_MS = '''\
<T>XDB</T>
<X>
com.microsoft.sqlserver.jdbc.SQLServerDriver
jdbc:sqlserver://127.0.0.1:1433;databaseName=test;user=sa;password=123456
</X>
'''

XDB_JDBC_MY = '''\
<T>XDB</T>
<X>
com.mysql.jdbc.Driver
jdbc:mysql://localhost/test?user=root&password=toor
</X>
'''

PHP_EXAMPLE = [PHP_MY, PHP_MY_LO, PHP_MY_OPT, PHP_MS, PHP_ORA, PHP_PG, PHP_INF]
ADO_EXAMPLE = [ADO_SQLSERVER, ADO_MY, ADO_ORA, ADO_ACCESS, ADO_OLEDB, ADO_OLEDB1, ADO_OLEDB4, ADO_DNS]
XDB_EXAMPLE = [XDB_JDBC_MY, XDB_JDBC_MS, XDB_SQLSERVER, XDB_JDBC_ORA]


class DBConfig(QDialog, Ui_Dialog):
    sig_conf_submit = Signal(str)

    def __init__(self, conf='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_submit.clicked.connect(self.on_submit_clicked)
        self.cbo_example.currentIndexChanged.connect(self.on_example_changed)
        if 'ADO' in conf:
            self.cbo_example.insertItems(1, [ex.replace('\n', '') for ex in ADO_EXAMPLE])
            conf = conf or ADO_DEFAULT
            self.conf = ADO_EXAMPLE
        elif 'XDB' in conf:
            self.cbo_example.insertItems(1, [ex.replace('\n', '') for ex in XDB_EXAMPLE])
            conf = conf or XDB_JDBC_MY
            self.conf = XDB_EXAMPLE
        else:
            self.cbo_example.insertItems(1, [ex.replace('\n', '') for ex in PHP_EXAMPLE])
            conf = conf or PHP_MY_LO
            self.conf = PHP_EXAMPLE
        self.edt_conf.insertPlainText(conf)

    def on_submit_clicked(self):
        if self.edt_conf.toPlainText():
            self.sig_conf_submit.emit(self.edt_conf.toPlainText())
            self.hide()

    def on_example_changed(self):
        self.edt_conf.appendPlainText('')
        self.edt_conf.insertPlainText(self.conf[self.cbo_example.currentIndex() - 1])
