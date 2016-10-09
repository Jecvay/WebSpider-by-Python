# coding=utf-8

"""
人物关系爬虫, 支持多实例并发
"""

import threading
import logging
from zhihu.login_manager import ZhihuLoginManager


class RelationSpider(threading.Thread):
    spider_id = 0               # 历史创建的线程数量, 包括已经销毁的
    spider_running_cnt = 0      # 正在运行的线程数量

    def __init__(self):
        super().__init__()
        RelationSpider.spider_id += 1
        self.thread_id = RelationSpider.spider_id
        self.log = logging.getLogger(__name__ + "[" + str(self.thread_id) + "]")

    @property
    def session(self):
        login_manager = ZhihuLoginManager()
        return login_manager.session

    def run(self):
        self.log.info('Thread started')
        res = self.session.get("http://www.zhihu.com")
        self.log.info(res.text)
        self.log.info('Thread ended')


