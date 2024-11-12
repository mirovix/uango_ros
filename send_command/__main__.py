import os
import sys
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_web_socket import CommandWebSocket
from command_main import CommandMain

if __name__ == '__main__':
    command_main = CommandMain(sys.argv)
    command = command_main()
    print(command)
    web_socket = CommandWebSocket(command.get_command_sequence())
    asyncio.run(web_socket())
    exit(0)
