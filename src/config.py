class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


def choise_config(environment):
    if environment == 'production':
        config = 'src.config.ProductionConfig'
    else:
        config = 'src.config.DevelopmentConfig'

    return config
