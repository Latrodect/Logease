import logging

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """
        Initializes the Logger with a specific name and sets up handlers and formatters.
        """
        self.logger = logging.getLogger("LoglessLogger")
        self.logger.setLevel(logging.DEBUG)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(CustomFormatter())  # Create an instance of CustomFormatter
        self.logger.addHandler(self.console_handler)

    def log(self, message, level="INFO"):
        """
        Logs a message with the given severity level.

        Args:
            message (str): The message to log.
            level (str): The severity level of the log message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        """
        level = level.upper()
        if level == "CRITICAL":
            self.logger.critical(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "INFO":
            self.logger.info(message)
        elif level == "DEBUG":
            self.logger.debug(message)
        else:
            raise ValueError(f"Unsupported log level: {level}")

    def info(self, message):
        """
        Logs a message with INFO severity.

        Args:
            message (str): The message to log.
        """
        self.log(message, "INFO")

    def error(self, message):
        """
        Logs a message with ERROR severity.

        Args:
            message (str): The message to log.
        """
        self.log(message, "ERROR")

    def critical(self, message):
        """
        Logs a message with CRITICAL severity.

        Args:
            message (str): The message to log.
        """
        self.log(message, "CRITICAL")
