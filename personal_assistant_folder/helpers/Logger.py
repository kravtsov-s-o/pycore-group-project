import logging


class MyLogger:
    def __init__(self, log_file='jarlis.log', level=logging.ERROR):
        logging.basicConfig(filename=log_file, level=level, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def error(self, message):
        self.logger.error(message)
