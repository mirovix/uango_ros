import unittest
from unittest.mock import patch

from uango_connector.main import WebSocketApp


class TestWebSocketApp(unittest.TestCase):

    @patch('uango_connector.main.sys.argv', ['main.py', 'test_command'])
    @patch('uango_connector.main.CommandMain')
    @patch('uango_connector.main.WebSocketConnection')
    @patch('uango_connector.main.dotenv_values', return_value={'IP_ADDRESS_UANGO': '127.0.0.1', 'PORT_UANGO': '8080'})
    def test_init(self, mock_dotenv_values, _, mock_command_main):
        app = WebSocketApp()
        self.assertEqual(app.args, 'test_command')
        self.assertEqual(app.socket_address, '127.0.0.1:8080')
        mock_command_main.assert_called_once_with('test_command')
        mock_dotenv_values.assert_called_once()

    @patch('uango_connector.main.sys.argv', ['main.py'])
    def test_check_command_empty(self):
        with self.assertRaises(SystemExit):
            WebSocketApp._check_command(['main.py'])

    @patch('uango_connector.main.dotenv_values', return_value={'IP_ADDRESS_UANGO': '127.0.0.1', 'PORT_UANGO': '8080'})
    def test_get_socket(self, mock_dotenv):
        socket = WebSocketApp._get_socket()
        self.assertEqual(socket, '127.0.0.1:8080')
        mock_dotenv.assert_called_once()

    @patch('uango_connector.main.CommandMain')
    @patch('uango_connector.main.asyncio.run')
    @patch('uango_connector.main.WebSocketConnection')
    @patch('uango_connector.main.ParserMain')
    def test_run(self, mock_parser_main, mock_web_socket_connection, mock_asyncio_run, _):
        mock_asyncio_run.return_value = 'response'
        app = WebSocketApp('test_command')
        app.run()
        mock_web_socket_connection.assert_called_once_with(app.command_sequence, app.socket_address)
        mock_parser_main.assert_called_once_with('response')
