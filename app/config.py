class Config:
    DEBUG = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ("postgresql://postgres:password@localhost/social")
    DEBUG = True
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = ("postgresql://postgres:password@localhost/social")

class DockerConfig(Config):
    SQLALCHEMY_DATABASE_URI = ("postgresql://postgres:password@postgres/social")

config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "docker": DockerConfig
}