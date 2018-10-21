import os

from mudao.utils.sqlite import SQLite as DB
from mudao.utils.logger import logger as log


class Box(object):

    def __init__(self, dbf='mudao.db'):
        self.db = self.init(dbf)
        self.shell_key = ['id', 'url', 'pwd', 'type', 'category', 'sqlconf', 'comment', 'geo', 'status', 'c_time', 'e_time']

    def init(self, dbf):
        if not os.path.exists(dbf):
            log.info('Init database...')
            sqlList = ["""\
            CREATE TABLE 'box' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'url' VARCHAR(128),
            'pwd' VARCHAR(8),
            'type' VARCHAR(4),
            'encoding' VARCHAR(16),
            'category' VARCHAR(32) default 'default',
            'sqlconf' TEXT,
            'tag' TEXT,
            'geo' VARCHAR(4),
            'status' VARCHAR(4),
            'c_time' TIMESTAMP not null default (datetime('now','localtime')),
            'e_time' TIMESTAMP not null default (datetime('now','localtime'))
            );
            """,
            # """\
            # CREATE TABLE 'group_list' (
            # 'group_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            # 'group_name' VARCHAR(64),
            # 'count' INT DEFAULT 0
            # );
            #
            # """,
            # """
            # insert into `group_list` ('group_name', 'count') value ('default', 0);
            # """
            """\
            CREATE TABLE 'site_cache' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'sid' INTEGER,
            'path' TEXT,
            'cache' BLOB
            );
            
            """,
            """\
            create trigger box_Update before update on box
            for each row
            begin
            update box set e_time = datetime('now','localtime') where id=old.id;
            end;
            """
            ]
            database = DB(dbf)
            for sql in sqlList:
                database.execute(sql)
        else:
            database = DB(dbf)

        return database

    def add_shell(self, shell):
        log.debug('Add shell: %s' % shell)
        self.db.insert('box', shell)

    def get_shell(self, sid=None):
        log.debug('Get shell with sid: %s' % sid)
        if isinstance(sid, int):
            return self.db.getOne('box', condition={'id': sid})
        elif isinstance(sid, dict):
            return self.db.getOne('box', condition=sid)
        return self.db.getList('box')

    def update_shell(self, sid, data):
        log.debug('Update shell %s with data: %s' % (sid, data))
        return self.db.update('box', data, dict(id=sid))

    def delete_shell(self, sid):
        log.delete('Delete shell %s' % sid)
        return self.db.delete('box', dict(id=sid))

    def add_path(self, sid, path, content):
        log.debug('Add site (%s) path (%s) cache (%)' % (sid, path, content))
        return self.db.insert('site_cache', dict(sid=sid, path=path, cache=content))

    def get_cache(self, sid, path):
        log.debug('Get site (%s) cache path (%)' % (sid, path))
        return self.db.getOne('site_cache', 'cache', dict(sid=sid, path=path))

    def update_cache(self, sid, path, content):
        log.debug('Update site (%s) path (%s) cache (%)' % (sid, path, content))
        return self.db.update('site_cache', dict(cache=content), dict(sid=sid, path=path))

    def delete_cache(self, sid, path=None):
        log.debug('Delete site (%s) path (%s) cache' % (sid, path))
        condition = dict(sid=sid, path=path) if path else dict(sid=sid)
        return self.db.delete('site_cache', condition)
