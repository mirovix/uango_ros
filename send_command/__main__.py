import asyncio
import os
import sys

from dotenv import dotenv_values

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_web_socket import CommandWebSocket
from command_main import CommandMain

if __name__ == '__main__':
    command_main = CommandMain(sys.argv)
    command = command_main()
    print(command)

    env = dotenv_values()
    ip = env['IP_ADDRESS']
    port = env['PORT']
    socket_address = str(ip) + ':' + str(port)
    web_socket = CommandWebSocket(command.get_command_sequence(), socket_address)
    asyncio.run(web_socket())
    exit(0)
