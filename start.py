# coding=utf-8

import logging
import config

from utils.singleton import singleton
from zhihu.login_manager import ZhihuLoginManager
from zhihu.relation_spider import RelationSpider


@singleton
class Launcher:
    def __init__(self):

        # 根日志设置
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-4s [%(name)s] %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='1.log',
                            filemode='w')

        # 控制台输出日志设置
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)-4s [%(name)s] %(message)s')
        formatter.datefmt = '%m-%d %H:%M'
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)

        # 属性
        self.login_manager = ZhihuLoginManager()
        self.login_manager.set_login_method('cookie')
        self.log = logging.getLogger(__name__)
        self.thread_list = []

    @property
    def session(self):
        return self.login_manager.session

    def run(self):
        self.login_manager.login()
        if self.session:
            # 成功登录
            self.log.info("Login Zhihu success!")
            for i in range(0, config.ZHIHU_RELATION_THREAD_NUMBER):
                self.thread_list.append(RelationSpider())

            for thread in self.thread_list:
                thread.run()

if __name__ == '__main__':
    launcher = Launcher()
    launcher.run()