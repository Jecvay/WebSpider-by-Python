# coding=utf-8

from login_manager_base import LoginManagerBase


class ZhihuLoginManager(LoginManagerBase):

	def __init__(self):
		super().__init__()
		self.url_root = 'www.zhihu.com'
		self.url_start = ''
		self.set_login_method('cookie')

	def _login_by_post(self):
		pass

	def _login_by_cookie(self):
		print ("login_by_cookie !!")


if __name__ == '__main__':
	login_manager = ZhihuLoginManager()
	login_manager.login()

