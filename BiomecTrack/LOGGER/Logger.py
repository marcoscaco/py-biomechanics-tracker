import logging


class Logger:
    logger: logging = None

    def __init__(self, logger_reference: logging, logger_level=logging.NOTSET):
        self.logger = logger_reference.getLogger('BM-Track-Log')
        self.logger.setLevel(logger_level)
        self.logger.info('Logger Iniciado')

    def log_into_warnning(self, mensage):
        self.logger.warning(mensage)

    def log_into_info(self, message):
        self.logger.info(message)