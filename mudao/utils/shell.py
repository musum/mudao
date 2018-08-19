import re


class Shell(object):
    def __init__(self, url, pwd, type):
        self.url = url
        self.pwd = pwd
        self.type = type
        self.conf = {}
        self.payload = None

    def generate_payload(self, fun='info', **kwargs):
        pass

    def load_conf(self, con):
        pass


