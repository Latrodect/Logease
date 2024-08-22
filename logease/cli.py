import argparse
from termcolor import colored, cprint
from logease.config.settings import LogConfig


class CommandLineInterface:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initializes the command-line interface.
        """
        self._print_banner()

    def _print_banner(self):
        "Prints the banner when the CLI Initialize"
        banner = """
          ___  _____ _____  ___ ______ _____ 
    /\   / _ \|  ___)  ___)/ _ \\  ___)  ___)
   /  \ | | | | |   | |_  | |_| |\ \  | |_   
  / /\ \| | | | |   |  _) |  _  | > > |  _)  
 / /  \ \ |_| | |   | |___| | | |/ /__| |___ 
/_/    \_\___/|_|   |_____)_| |_/_____)_____)
                                             
Bahadir NURAL - MIT License.


"""
        cprint(banner, "light_green")
        cprint("Logease is CLI Tools for Configure logease package.", "white")

    def show_available_configuration(self):
        description = """

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
        """

        print(description)

    def show_commands(self):
        help = """
Available Commands:

1. **help**: 
   - Displays this help text.
   - Example: `logease help`

2. **available**: 
   - Lists all available configuration options that you can modify.
   - Example: `logease available`

3. **config**: 
   - Updates the configuration attribute of the instance based on the provided key-value pair.
   - Example: `logease config`

Usage Examples:

- To see the list of commands: `help`
- To view all configurable options: `available`

Supported configuration keys include options like "level", "log_format", "splunk_host", and more.
Use the `available` command to see the full list.
    """

        print(help)

    def run(self):
        parser = argparse.ArgumentParser(description="Logease: Configure your logger.")
        sub_parsers = parser.add_subparsers(dest="command", help="Available commands")

        config_command_parser = sub_parsers.add_parser(
            "config", help="Configuration for logease middleware"
        )
        available_command_parser = sub_parsers.add_parser(
            "available", help="Show available edit options for config."
        )

        help_command_parser = sub_parsers.add_parser(
            "help", help="Show available commands."
        )

        args = parser.parse_args()

        if args.command == "config":
            while True:
                
                print(colored("\nConfiguration Field: ", "light_green"), end="")
                field = input()

                print(colored("Field Value: ", "light_green"), end="")
                value = input()

                print(colored("Quit (type 'y/yes'): ", "light_green"), end="")
                quit = input()

                config_instance = LogConfig()
                config_instance.change_config_values(field, value)

                if quit.lower() == "y" or quit.lower() == "yes":
                    break

        elif args.command == "available":
            self.show_available_configuration()

        elif args.command == "help":
            self.show_commands()


def main():
    """
    Entry point of the CLI application
    """
    cli = CommandLineInterface()
    cli.run()


if __name__ == "__main__":
    main()
