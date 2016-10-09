# coding=utf-8

"""
通用登录类, 可通过继承与重写来适应不同网站
"""

import abc


class LoginManagerBase:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.url_root = None
        self.url_start = None
        self.login = lambda: (_ for _ in ()).throw(Exception("LoginManager.login not define"))

    @abc.abstractmethod
    def _login_by_post(self):
        pass

    @abc.abstractmethod
    def _login_by_cookie(self):
        pass

    def set_login_method(self, method):
        if method == 'cookie':
            self.login = self._login_by_cookie
        elif method == 'post':
            self.login = self._login_by_post
        else:
            raise Exception("set_login_method invalid method")
