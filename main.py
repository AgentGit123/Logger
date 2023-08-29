# 读取yaml配置文件
import yaml
f = open('config_dev.yaml','r',encoding='utf8')
data = f.read()
f.close()
# print(data)
config = yaml.load(data,Loader=yaml.FullLoader)
# print(config)
logOutType = config["log_param"]["log_out_type"]
logPath = config["log_param"]["log_path"]
logFileName = config["log_param"]["log_file_name"]
logLevel = config["log_param"]["log_level"]
logMaxFileNum = config["log_param"]["log_max_file_num"]
logMaxFileSize = config["log_param"]["log_max_file_size"]


# 创建日志类对象
from MyLogger import Logger
logger = Logger(logPath, logFileName, logMaxFileSize, logMaxFileNum, logOutType, logLevel).getLogger()

logger.debug("debug")
logger.info("info")
logger.warn("warn")
logger.error("error")
logger.critical("critical")