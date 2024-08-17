import os

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



