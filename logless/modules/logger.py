import logging
from logless.handlers.request import SplunkHandler, ElasticSearchHandler, APIHandler, EmailHandler, SNMPHandler
from logless.config.settings import LogConfig

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
        self.console_handler.setFormatter(CustomFormatter())  
        self.logger.addHandler(self.console_handler)
        self.setup()

    def setup(self):
        """
        Configures logging handlers based on the current log configuration.

        This method initializes the logging system based on the logging destination specified in the `LogConfig` instance.
        It sets up appropriate handlers for different logging destinations such as Splunk, Elasticsearch, API endpoints,
        local files, email, and SNMP traps. Each handler is configured with a custom formatter and added to the logger.

        The method performs the following steps:
        1. Retrieves the log destination and related configuration from `LogConfig`.
        2. Based on the destination, it creates and configures the appropriate logging handler:
            - **Splunk**: Configures a `SplunkHandler` if Splunk host and token are provided.
            - **Elasticsearch**: Configures an `ElasticSearchHandler` if Elasticsearch host and index are provided.
            - **API**: Configures an `APIHandler` if an API endpoint and key are provided.
            - **Local File**: Configures a `FileHandler` if a local file path is specified.
            - **Email**: Configures an `EmailHandler` if email recipients and SMTP server details are provided.
            - **SNMP**: Configures an `SNMPHandler` if an SNMP trap receiver and community details are provided.
        3. Adds each configured handler to the logger with a custom formatter for consistent log formatting.

        This method assumes that `LogConfig` has already been instantiated and populated with necessary environment variables.
        """
        log_config = LogConfig() 

        log_destination = log_config.get_log_destination()
        
        if log_destination == 'splunk' and log_config.splunk_host and log_config.splunk_token:
            splunk_handler = SplunkHandler(log_config.splunk_host, log_config.splunk_token)
            splunk_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(splunk_handler)

        elif log_destination == 'elasticsearch' and log_config.elastic_host and log_config.elastic_index:
            elastic_handler = ElasticSearchHandler(log_config.elastic_host, log_config.elastic_index)
            elastic_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(elastic_handler)

        elif log_destination == 'api' and log_config.api_endpoint and log_config.api_key:
            api_handler = APIHandler(log_config.api_endpoint, log_config.api_key)
            api_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(api_handler)

        elif log_destination == 'local_file' and log_config.local_file_path:
            file_handler = logging.FileHandler(log_config.local_file_path)
            file_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(file_handler)

        elif log_destination == 'email' and log_config.email_recipients:
            email_handler = EmailHandler(
                smtp_server=log_config.smtp_server,
                smtp_port=log_config.smtp_port,
                from_addr=log_config.email_from,
                to_addrs=log_config.email_recipients.split(','),
                subject='Log Notification',
                username=log_config.smtp_username,
                password=log_config.smtp_password
            )
            email_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(email_handler)

        elif log_destination == 'snmp' and log_config.snmp_trap_receiver:
            snmp_handler = SNMPHandler(
                trap_receiver=log_config.snmp_trap_receiver,
                community=log_config.snmp_community,
                port=log_config.snmp_port
            )
            snmp_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(snmp_handler)

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
