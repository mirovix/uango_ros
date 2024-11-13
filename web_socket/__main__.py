import asyncio
import os
import sys

from dotenv import dotenv_values

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from text_parser.parser_main import ParserMain
from send_command.command_main import CommandMain
from web_socket.web_socket_main import WebSocketMain

if __name__ == '__main__':
    command_main = CommandMain(sys.argv)
    command = command_main()
    print(command)

    env = dotenv_values()
    socket_address = str(env['IP_ADDRESS']) + ':' + str(env['PORT'])
    command_sequence = command.get_command_sequence()
    web_socket = WebSocketMain(command_sequence, socket_address)
    response = asyncio.run(web_socket())

    if response is not None:
        parser_main = ParserMain(response)
        parser_main()
        print(parser_main)

    exit(0)
