# -*- coding: utf-8 -*-
# File : logs.py
# Author: Off
# Date : 2022/2/12
# Desc : 日志

import logging
import os
import time


class Logging(object):
    def __init__(self):
        timestamp = time.strftime('%Y-%m-%d %H%M%S')
        filedir = os.path.join(os.path.dirname(__file__), '../logs')
        filename = os.path.abspath(filedir + '/' + timestamp + '.log')

        self.logger = logging.getLogger()
        self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        fh = logging.FileHandler(filename=filename, encoding='UTF-8')
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")

        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


if __name__ == '__main__':

    log = Logging().logger
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
