import inspect
import logging


class  LogGen:
        @staticmethod
        def loggen():
            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)
            fileHandler = logging.FileHandler('C:\\Users\\SHADAB\\PycharmProjects\\Upload\\Logs\\automationlog.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)  # filehandler object

            logger.setLevel(logging.DEBUG)
            logger.error("Your error message!")
            logger.critical("Your critical message!")
            logger.debug("Your debug message!")
            logger.info("Your info message!")
            logger.warning("Your warning message!")
            return logger
