from logging import (
    basicConfig,
    DEBUG,
    INFO,
    ERROR,
    debug,
    info,
    error,
    FileHandler,
    StreamHandler
)

def config_logger():

    basicConfig(
        level=INFO,
        encoding='utf-8',
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    return