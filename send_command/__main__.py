import asyncio
import os
import socket
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_web_socket import CommandWebSocket
from command_main import CommandMain

if __name__ == '__main__':
    command_main = CommandMain(sys.argv)
    command = command_main()
    print(command)

    ip = os.getenv('IP_ADDRESS', '192.168.12.1')
    port = os.getenv('PORT', 8080)
    socket_address = ip + ':' + str(port)
    web_socket = CommandWebSocket(command.get_command_sequence(), socket_address)
    asyncio.run(web_socket())
    exit(0)
