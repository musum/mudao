

class Shell(object):

    def __init__(self, **kwargs):
        self._id = kwargs.get('id', None)
        self._url = kwargs.get('url', '')
        self._pwd = kwargs.get('pwd', '')
        self._type = kwargs.get('type', '')
        self._encoding = kwargs.get('encoding', '')
        self._sqlconf = kwargs.get('sqlconf', '')
        self._group = kwargs.get('category', 'default')
        self._tag = kwargs.get('tag', '')
        self._status = None

    def get_id(self):
        return self._id

    def to_dict(self):
        return dict(url=self.url, pwd=self.pwd, type=self.type, encoding=self.encoding,
                    sqlconf=self.sqlconf, category=self.category, tag=self.tag)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, u):
        self._url = u

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, p):
        self._pwd = p

    @property
    def encoding(self):
        return self._encoding

    @encoding.setter
    def encoding(self, enc):
        self._encoding = enc

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, ty):
        self._type = ty

    @property
    def sqlconf(self):
        return self._sqlconf

    @sqlconf.setter
    def sqlconf(self, conf):
        self._sqlconf = conf

    @property
    def category(self):
        return self._group

    @category.setter
    def category(self, g):
        self._group = g

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, tag):
        self._tag = tag

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self._status = status
