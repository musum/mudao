from mudao.utils.tool import parse_caidao


class Shell(object):
    def __init__(self, url, pwd, type):
        self.url = url
        self.pwd = pwd
        self.type = type
        self.conf = parse_caidao('caidao.conf')
        self.payload = None

    def generate_payload(self, fun='info', **kwargs):
        pass

    @staticmethod
    def load_conf(con):
        pass


