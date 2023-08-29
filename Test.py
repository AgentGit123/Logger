import logging

logger = logging.getLogger(__name__)
import logutil2

if __name__ == '__main__':
    logger = logutil2.logs().getLogger()

    # a = [1,2,3]
    # logger.info("list a only have 1,2,3")
    # logger.warning("操作不当可能导致错误发生")
    # try:
    #     print(a[3])
    #     logger.debug("this is debug")
    # except Exception as e:
    #     logger.error(e)
    # finally:
    #     logger.info("无论如何需要执行此")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    # logger.critical("critical")