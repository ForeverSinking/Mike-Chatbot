import os

from datetime import datetime
from pydantic_settings import BaseSettings

class Config(BaseSettings):

    """
    配置类，继承自BaseSettings，用于存储应用程序的各种配置参数
    """
    # 项目地址
    SERVER_PATH: str = os.path.dirname(os.path.abspath(__file__))       # 项目地址：获取当前文件所在目录的绝对路径
    PROJECT_NAME: str = os.path.basename(os.getcwd())                   # 项目名称：获取当前工作目录的名称

    # 日志配置
    LOG_DIR: str = f"{SERVER_PATH}/logs"                                                          # log 存储目录：日志文件保存的路径
    LOG_LEVEL: str = "DEBUG"                                                                      # 日志等级：设置日志记录的级别为DEBUG
    LOG_ROTATION: str = "10 MB"                                                                   # 日志文件大小达到 10MB 时轮转：单个日志文件的最大大小
    LOG_BACKUP_COUNT: int = 7                                                                     # 保留日志文件个数：保留的日志文件数量
    LOG_COLOR: bool = True                                                                        # 是否启用彩色日志
    LOG_FILE_ZIP: bool = True                                                                     # 是否启用日志文件压缩：控制日志文件是否被压缩
    LOG_FILE: str = f"{SERVER_PATH}/logs/{PROJECT_NAME}_{datetime.now().strftime('%Y%m%d')}.log"  # 日志文件：日志文件的完整路径，包含项目名称和当前日期
    LOG_FORMAT: str = (                                                                           # 日志格式：定义日志输出的格式
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <4}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>line:{line}</cyan> | <level>{message}</level>"
    )                                                                                   




config = Config()
