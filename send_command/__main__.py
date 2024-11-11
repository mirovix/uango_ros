import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_main import CommandMain

if __name__ == '__main__':
    command_main = CommandMain(sys.argv)
    command = command_main()
    print(command)
