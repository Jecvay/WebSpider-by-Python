# coding=utf-8

from login_manager_base import LoginManagerBase
from utils.singleton import singleton
import requests
import config
import logging


@singleton
class ZhihuLoginManager(LoginManagerBase):
    """
        登录之后, 就可以获取 session 来进行网络操作
    """

    def __init__(self):
        super().__init__()
        self.url_root = 'https://www.zhihu.com'
        self.url_start = ''
        self.cookie = {}
        self.log = logging.getLogger(__name__)

    def _login_by_post(self):
        pass

    def _login_by_cookie(self):
        """
            关于知乎 cookie 的说明:
                1. 在浏览器控制台中执行 console.log(document.cookie)
                2. 找到 z_c0 & login 两部分复制过来
        """
        self.log.info('login by cookie')
        self.cookie['login'] = config.ZHIHU_COOKIE_LOGIN
        self.cookie['z_c0'] = config.ZHIHU_COOKIE_Z0
        cookie_jar = requests.utils.cookiejar_from_dict(self.cookie)
        self._session = requests.Session()
        self._session.headers['User-Agent'] = config.USER_AGENT
        self._session.cookies = cookie_jar
        if not self._check_connection():
            self._session = None

    def _check_connection(self):
        return True


if __name__ == '__main__':

    # 测试登录知乎
    login_manager = ZhihuLoginManager()
    login_manager.set_login_method('cookie')
    login_manager.login()
    res = login_manager.session.get("http://www.zhihu.com")
    print(res.text)