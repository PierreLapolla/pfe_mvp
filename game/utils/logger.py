import logging
from logging.handlers import QueueHandler, QueueListener
from pathlib import Path
from queue import Queue


class LoggerSingleton:
    """
    Singleton class to initialize and manage the application logger with asynchronous logging support.
    A new log file is created for each application run.
    """
    _instance = None

    def __new__(cls, log_level=logging.INFO) -> 'LoggerSingleton':
        """
        Create a new instance of LoggerSingleton if it doesn't exist.

        :param log_level: The logging level to be set for the logger.
        :return: The singleton instance of LoggerSingleton.
        """
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)

            log_file = Path('logs/app.log')
            log_file.parent.mkdir(parents=True, exist_ok=True)
            if log_file.exists():
                log_file.unlink()

            log_queue = Queue()

            cls._instance.logger = logging.getLogger('app_logger')
            cls._instance.logger.setLevel(log_level)

            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(log_level)

            log_format = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s'
            formatter = logging.Formatter(log_format)
            file_handler.setFormatter(formatter)

            queue_handler = QueueHandler(log_queue)
            cls._instance.logger.addHandler(queue_handler)

            listener = QueueListener(log_queue, file_handler)
            listener.start()

            cls._instance.listener = listener

        return cls._instance

    def get_logger(self) -> logging.Logger:
        """
        Get the logger instance.

        :return: The logger instance.
        """
        return self.logger


log = LoggerSingleton(log_level=logging.DEBUG).get_logger()

# Usage example:
if __name__ == "__main__":
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
