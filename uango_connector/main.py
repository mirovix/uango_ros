import asyncio
import os
import sys

from dotenv import dotenv_values

from uango_connector.send_command.command_main import CommandMain
from uango_connector.text_parser.parser_main import ParserMain
from uango_connector.web_socket_connection import WebSocketConnection


class WebSocketApp:
    def __init__(self, args=None):
        if args is None:
            args = (self._check_command(sys.argv))
        self.args = args
        self.command_main = CommandMain(args)
        self.command = self.command_main()
        self.socket_address = self._get_socket()
        self.command_sequence = self.command.get_command_sequence()

    @staticmethod
    def _get_socket():
        env = dotenv_values()
        if 'IP_ADDRESS_UANGO' not in env or 'PORT_UANGO' not in env:
            env = os.environ
        return str(env['IP_ADDRESS_UANGO']) + ':' + str(env['PORT_UANGO'])

    @staticmethod
    def _check_command(args: list) -> str:
        if len(args) < 2:
            print("Empty command")
            exit(1)
        return args[1]

    def run(self):
        print(self.command)
        web_socket = WebSocketConnection(self.command_sequence, self.socket_address)
        response = asyncio.run(web_socket())

        if response and str(response).strip():
            parser_main = ParserMain(response)
            parser_main()
            print(parser_main)
