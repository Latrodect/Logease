import argparse
from termcolor import cprint


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
                                             

Logease is CLI Tools for Configure logease package.
"""

        cprint(banner, "light_red")

    def run(self):
        parser = argparse.ArgumentParser(description="Logease: Configure your logger.")
        sub_parsers = parser.add_subparsers(dest="command", help="Avaiable commands")

        sub_parsers.add_parser("edit", help="Configuration for logease middleware")

        args = parser.parse_args()

        if args.command == "config":
            field = input("Configuration Field:")
            # TODO: implement change config logic in here.


def main():
    """
    Entry point of the CLI application
    """
    cli = CommandLineInterface()
    cli.run()


if __name__ == "__main__":
    main()