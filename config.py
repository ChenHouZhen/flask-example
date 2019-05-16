# 全局配置文件
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 此处定义一些全局配置

    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevConfig(Config):
    pass


# 测试环境
class TestConfig(Config):
    pass


# 生产环境
class ProConfig(Config):
    pass


config = {
    'dev':DevConfig,
    'test':TestConfig,
    'pro':ProConfig,
    'default':DevConfig
}