# -*- encoding: utf-8 -*-
'''
@File      :   logger.py
@Time      :   2025/09/10 18:08:02
@Author    :   mike
@Version   :   1.0
@Contact   :   2140585762@qq.com
@Pip Proxy :   https://pypi.tuna.tsinghua.edu.cn/simple/
@Desc      :   
'''
import os
import sys

from loguru import logger

from config import config


class LoggerManager:
    """
    使用 Loguru 封装的日志管理器
    支持控制台输出、文件记录、日志轮转和不同日志级别
    """
    def __init__(self) -> None:
        # 移除 loguru 的默认配置
        logger.remove()
        self.compression = "zip" if config.LOG_FILE_ZIP else None

    def setup_logger(self):
        """创建日志目录"""
        if os.path.exists(config.LOG_DIR) is False:
            os.makedirs(config.LOG_DIR)
            logger.info(f"创建日志目录: {config.LOG_DIR}")

        """设置控制台日志"""
        logger.add(
            sink=sys.stderr,            # 控制台输出
            format=config.LOG_FORMAT,   # 日志格式
            level=config.LOG_LEVEL,     # 日志等级
            colorize=config.LOG_COLOR,  # 启用彩色输出
            backtrace=True,             # 允许显示异常回溯
            diagnose=True               # 显示变量值以便调试
        )
        """设置文件日志"""
        logger.add(
            sink=config.LOG_FILE,               # 日志文件路径
            format=config.LOG_FORMAT,           # 日志格式
            level=config.LOG_LEVEL,             # 日志等级
            rotation=config.LOG_ROTATION,       # 日志轮转
            retention=config.LOG_BACKUP_COUNT,  # 日志保留数量
            compression=self.compression,       # 轮转的日志文件使用 zip 压缩
            encoding="utf-8",                   # 文件编码
            enqueue=True                        # 线程安全
        )
        logger.info("日志器初始化完成")
        return logger

logger_manager = LoggerManager()
logger = logger_manager.setup_logger()

if __name__ == "__main__":
    logger.info("主程序启动")