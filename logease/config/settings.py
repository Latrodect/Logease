import os
from termcolor import cprint
class LogConfig:
    def __init__(self) -> None:
        self.log_level = os.getenv("LOG_LEVEL", "DEBUG")
        self.log_format = os.getenv("LOG_FORMAT", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        self.splunk_host = os.getenv('SPLUNK_HOST', None)
        self.splunk_token = os.getenv('SPLUNK_TOKEN', None)
        self.elastic_host = os.getenv('ELASTIC_HOST', None)
        self.elastic_index = os.getenv('ELASTIC_INDEX', None)
        self.api_endpoint = os.getenv('API_ENDPOINT', None)
        self.api_key = os.getenv('API_KEY', None)
        self.local_file_path = os.getenv('LOCAL_FILE_PATH', 'logs/app.log')
        self.database_uri = os.getenv('DATABASE_URI', None)
        self.cloud_storage_bucket = os.getenv('CLOUD_STORAGE_BUCKET', None)
        self.syslog_server = os.getenv('SYSLOG_SERVER', None)
        self.log_aggregation_service = os.getenv('LOG_AGGREGATION_SERVICE', None)
        self.email_recipients = os.getenv('EMAIL_RECIPIENTS', None)
        self.smtp_server = os.getenv('SMTP_SERVER', None)
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.email_from = os.getenv('EMAIL_FROM', None)
        self.smtp_username = os.getenv('SMTP_USERNAME', None)
        self.smtp_password = os.getenv('SMTP_PASSWORD', None)
        self.message_queue = os.getenv('MESSAGE_QUEUE', None)
        self.websocket_url = os.getenv('WEBSOCKET_URL', None)
        self.snmp_trap_receiver = os.getenv('SNMP_TRAP_RECEIVER', None)
        self.snmp_community = os.getenv('SNMP_COMMUNITY', 'public')
        self.snmp_port = int(os.getenv('SNMP_PORT', 162))

        self.override_configs()

    def override_configs(self):
        if os.getenv('USE_SPLUNK', 'false').lower() == 'true':
            self.log_destination = 'splunk'
        elif os.getenv('USE_ELASTIC', 'false').lower() == 'true':
            self.log_destination = 'elasticsearch'
        elif os.getenv('USE_API', 'false').lower() == 'true':
            self.log_destination = 'api'
        elif os.getenv('USE_LOCAL_FILE', 'false').lower() == 'true':
            self.log_destination = 'local_file'
        elif os.getenv('USE_DATABASE', 'false').lower() == 'true':
            self.log_destination = 'database'
        elif os.getenv('USE_CLOUD_STORAGE', 'false').lower() == 'true':
            self.log_destination = 'cloud_storage'
        elif os.getenv('USE_SYSLOG', 'false').lower() == 'true':
            self.log_destination = 'syslog'
        elif os.getenv('USE_LOG_AGGREGATION', 'false').lower() == 'true':
            self.log_destination = 'log_aggregation'
        elif os.getenv('USE_EMAIL', 'false').lower() == 'true':
            self.log_destination = 'email'
        elif os.getenv('USE_MESSAGE_QUEUE', 'false').lower() == 'true':
            self.log_destination = 'message_queue'
        elif os.getenv('USE_WEBSOCKET', 'false').lower() == 'true':
            self.log_destination = 'websocket'
        elif os.getenv('USE_SNMP', 'false').lower() == 'true':
            self.log_destination = 'snmp'
        else:
            self.log_destination = 'console'

    def get_log_destination(self):
        return self.log_destination
    
    def change_config_values(self, key, value):
        """
        Update the configuration attribute of the instance based on the provided key-value pair.

        This method allows dynamic updating of configuration attributes within the instance. 
        The `key` parameter determines which configuration attribute to update, and the `value`
        parameter provides the new value for that attribute. 

        Supported keys include:
            - "level": Updates the logging level.
            - "log_format": Sets the format for log messages.
            - "splunk_host", "splunk_token": Configures Splunk logging.
            - "elastic_host", "elastic_index": Configures Elasticsearch logging.
            - "api_endpoint", "api_key": Sets the API endpoint and key for external logging.
            - "local_file_path": Updates the file path for local logging.
            - "database_uri": Sets the database URI for log storage.
            - "cloud_storage_bucket": Configures the cloud storage bucket for logs.
            - "syslog_server": Sets the Syslog server address.
            - "log_aggregation_service": Configures the log aggregation service.
            - "email_recipients", "smtp_server", "smtp_port", "email_from", "smtp_username", "smtp_password":
                Configures email settings for log notifications.
            - "message_queue": Sets the message queue for log handling.
            - "websocket_url": Configures the WebSocket URL for log streaming.
            - "snmp_trap_receiver", "snmp_community", "snmp_port": Configures SNMP settings.

        If the provided `key` does not match any of the supported attributes, a KeyError is raised.

        Parameters:
            key (str): The name of the configuration attribute to update.
            value (str): The new value for the configuration attribute.

        Raises:
            KeyError: If the provided `key` does not match any of the supported configuration attributes.
    """
        config_map = {
            "level": lambda v: setattr(self, 'log_level', v),
            "log_format": lambda v: setattr(self, 'log_format', v),
            "splunk_host": lambda v: setattr(self, 'splunk_host', v),
            "splunk_token": lambda v: setattr(self, 'splunk_token', v),
            "elastic_host": lambda v: setattr(self, 'elastic_host', v),
            "elastic_index": lambda v: setattr(self, 'elastic_index', v),
            "api_endpoint": lambda v: setattr(self, 'api_endpoint', v),
            "api_key": lambda v: setattr(self, 'api_key', v),
            "local_file_path": lambda v: setattr(self, 'local_file_path', v),
            "database_uri": lambda v: setattr(self, 'database_uri', v),
            "cloud_storage_bucket": lambda v: setattr(self, 'cloud_storage_bucket', v),
            "syslog_server": lambda v: setattr(self, 'syslog_server', v),
            "log_aggregation_service": lambda v: setattr(self, 'log_aggregation_service', v),
            "email_recipients": lambda v: setattr(self, 'email_recipients', v),
            "smtp_server": lambda v: setattr(self, 'smtp_server', v),
            "smtp_port": lambda v: setattr(self, 'smtp_port', int(v)),
            "email_from": lambda v: setattr(self, 'email_from', v),
            "smtp_username": lambda v: setattr(self, 'smtp_username', v),
            "smtp_password": lambda v: setattr(self, 'smtp_password', v),
            "message_queue": lambda v: setattr(self, 'message_queue', v),
            "websocket_url": lambda v: setattr(self, 'websocket_url', v),
            "snmp_trap_receiver": lambda v: setattr(self, 'snmp_trap_receiver', v),
            "snmp_community": lambda v: setattr(self, 'snmp_community', v),
            "snmp_port": lambda v: setattr(self, 'snmp_port', int(v)),
        }
        
        if key in config_map:
            config_map[key](value)
        else:
            cprint(f"\nUnknown configuration key: {key}", "light_red")


