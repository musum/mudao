import sqlite3 as db

from mudao.utils.logger import logger as log


class SQLite:
    def __init__(self, dbf):
        self.conn = db.connect(dbf)
        self.cursor = self.conn.cursor()

    def fetchAll(self, sql, data=[]):
        result = None
        if self.cursor.execute(sql, list(data)):
            result = self.cursor.fetchall()
            if len(result) > 0:
                return [dict(zip([j[0] for j in self.cursor.description], i)) for i in result]
        return result

    def fetchOne(self, sql, data=[]):
        result = None
        if self.cursor.execute(sql, list(data)):
            result = self.cursor.fetchone()
            if result != None:
                return dict(zip([j[0] for j in self.cursor.description], result))
        return result

    def getList(self, tableName, colums="*", condition="", orders="", limits=""):
        sql = "SELECT "+colums+" FROM " + tableName + " WHERE 1=1"
        _data = []
        if type(condition) == dict:
            for i in condition.keys():
                sql += " AND "+i+"=?"
            _data = condition.values()
        else:
            sql += condition
        sql += " order by "+orders if orders else ""
        sql += " limit "+limits if limits else ""
        result = self.fetchAll(sql, _data)
        return [] if result is None else result

    def getOne(self, tableName, colums="*", condition="", orders="", limits=""):
        sql = "SELECT "+colums+" FROM " + tableName + " WHERE 1=1"
        _data = []
        if type(condition) == dict:
            for i in condition.keys():
                sql += " AND "+i+"=?"
            _data = condition.values()
        else:
            sql += condition
        sql += " order by "+orders if orders else ""
        sql += " limit "+limits if limits else ""
        return self.fetchOne(sql, _data)

    def insert(self, tableName, data):
        sql = "INSERT INTO " + tableName + " ("+",".join(data.keys())+") VALUES ("+("?,"*len(data))[:-1]+")"
        status = self.execute(sql, data.values())
        # status = self.cursor.execute(sql, data.values())
        # self.conn.commit()
        return status

    def delete(self, tableName, condition):
        sql = "DELETE FROM " + tableName + " WHERE 1=1"
        _data = []
        if type(condition) == dict:
            for i in condition.keys():
                sql += " AND "+i+"=?"
            _data = condition.values()
        else:
            sql += condition
        status = self.execute(sql, _data)
        # status = self.cursor.execute(sql, _data)
        # self.conn.commit()
        return status

    def update(self, tableName, data, condition):
        sql = "UPDATE " + tableName + " SET "
        _data = []
        #update data
        if type(data) == dict:
            for i in data.keys():
                sql += i+"=?,"
            sql = sql[:-1]
            _data = data.values()
        else:
            sql = sql + data
        #condition
        sql += " WHERE 1=1 "
        if type(condition) == dict:
            for i in condition.keys():
                sql += " AND "+i+"=?"
            _data += condition.values()
        else:
            sql = sql + condition
        status = self.execute(sql, _data)
        # status = self.cursor.execute(sql, _data)
        # self.conn.commit()
        return status

    def execute(self, sql, data=[]):
        data = tuple(data)
        st = 'Excute sql: %s with data %s' if data else 'Excute sql: %s'
        log.debug(st % (sql, data))
        status = self.cursor.execute(sql, list(data))
        self.conn.commit()
        return status