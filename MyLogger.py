import logging
import logging.handlers
import os



class Logger:
    Level = 0
    def __init__(self, logPath, logFileName, logMaxFileSize, logMaxFileNum, logOutType,
                 logLevel):
        self.logger = logging.getLogger("")

        # 创建文件目录
        logs_dir = logPath
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)

        # 修改log保存位置
        logfilename = '%s.txt' % logFileName
        logfilepath = os.path.join(logs_dir, logfilename)
        # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=logMaxFileSize * 1024 * 1024,
                                                                   backupCount=logMaxFileNum)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(filename)s] [%(lineno)d] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # '[%(asctime)s] [%(filename)s] [%(lineno)d] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S,%f'
        rotatingFileHandler.setFormatter(formatter)

        # 设置对应的日志级别

        if logLevel == "DEBUG":
            global Level
            Level = 10
        elif logLevel == "INFO":
            Level = 20
        elif logLevel == "WARNING":
            Level = 30
        elif logLevel == "ERROR":
            Level = 40
        elif logLevel == "CRITICAL":
            Level = 50
        else:
            Level = 0

        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(Level)
        console.setFormatter(formatter)

        # 添加内容到日志句柄中
        # 日志输出保存通过配置文件配置可以有三种方式：只输出到屏幕；只输出保存到文件；同时输出到屏幕和文件中
        if logOutType == "all":
            self.logger.addHandler(rotatingFileHandler)
            self.logger.addHandler(console)
        elif logOutType == "file":
            self.logger.addHandler(rotatingFileHandler)
        else:
            self.logger.addHandler(console)
        self.logger.setLevel(Level)

    def getLogger(self):
        return self

    def debug(self, message):
            self.logger.debug(message)

    def info(self, message):
            self.logger.info(message)

    def warn(self, message):
            self.logger.warning(message)

    def error(self, message):
            self.logger.error(message)

    def critical(self, message):
            self.logger.critical(message)