# -*- coding:utf-8 -*-
"""
@author: GXJ
@file: log_helper.py
@time: 2020/8/16 19:27
@desc: log function
"""
from logging.handlers import TimedRotatingFileHandler
import logging
import re


def logger(filename):
    # 获取一个新的日志 指定输出信息模板
    logger = logging.getLogger('xingtu')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - [%(lineno)d] - %(message)s')
    # Test
    log_file_handler = TimedRotatingFileHandler(filename=filename, when="D", interval=30, backupCount=2)

    # log_file_handler = TimedRotatingFileHandler(filename="/var/weiboyi/azkaban/Crawler2/RegularTask/TrinityXingtuCrawler/xingtu/log/xingtu", when="D", interval=30, backupCount=2)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    logger.addHandler(log_file_handler)
    return logger
