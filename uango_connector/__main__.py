import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from uango_connector.main import WebSocketApp

if __name__ == '__main__':
    web_socket_app = WebSocketApp()
    web_socket_app.run()
    exit(0)
