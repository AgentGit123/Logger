# import logging, time
#
# log_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 获取当前日期
# # print(log_time)
# logging.basicConfig(level=logging.INFO, filename=log_time + '.log')  # 创建日志文件
# logging.info('%s 程序开始...' % time.ctime())  # 写入日志记录
#
# try:
#     for i in range(-5, 5):
#         logging.info('正在计算 12 /%d ...' % i)  # 写入日志记录
#         print(12 / i)
# except Exception as e:
#     logging.info('发生错误：' + str(e))  # 写入日志记录
#     raise
# logging.info('%s 程序结束...' % time.ctime())  # 写入日志记录


# import logging
#
# #设置输出格式
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# logger = logging.getLogger(__name__)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

import logging
import logging.handlers
import os
import time


class logs(object):
    def __init__(self):
        # 获取模块名称，测试的时候直接控模块即可，但是在实际使用的情况下需要针对不同需要进行日志撰写的模块进行命名
        # 列如：通讯协议模块，测试模块，数据库模块，业务层模块，API调用模块
        # 可以考虑 __init__(self,model_name) 这样传入，然后再用一个list规定一下模块名称
        self.logger = logging.getLogger("")
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # 创建文件目录
        logs_dir = "logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.txt' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def getLogger(self):
        return self

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)