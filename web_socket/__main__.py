import asyncio
import os
import sys

from dotenv import dotenv_values

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_socket.text_parser.parser_main import ParserMain
from web_socket.send_command.command_main import CommandMain
from web_socket.web_socket_main import WebSocketMain


def get_socket():
    env = dotenv_values()
    if 'IP_ADDRESS_UANGO' not in env or 'PORT_UANGO' not in env:
        env = os.environ
    return str(env['IP_ADDRESS_UANGO']) + ':' + str(env['PORT_UANGO'])


if __name__ == '__main__':
    command_main = CommandMain(sys.argv)
    command = command_main()
    print(command)

    socket_address = get_socket()
    command_sequence = command.get_command_sequence()
    web_socket = WebSocketMain(command_sequence, socket_address)
    response = asyncio.run(web_socket())

    if response and str(response).strip():
        parser_main = ParserMain(response)
        parser_main()
        print(parser_main)

    exit(0)
