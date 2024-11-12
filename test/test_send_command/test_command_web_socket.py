import unittest
from unittest.mock import AsyncMock, patch

from send_command.command_web_socket import CommandWebSocket


class TestCommandWebSocket(unittest.IsolatedAsyncioTestCase):

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenCommandSequence_whenCallingCommandWebSocket_thenReturnTrue(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = CommandWebSocket(command_sequence)

        mock_websocket = AsyncMock()
        mock_connect.return_value = mock_websocket

        result = await command_websocket()
        self.assertTrue(result)

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenWrongWebSocketOutput_whenCallingCommandWebSocket_thenReturnFalse(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = CommandWebSocket(command_sequence, "ws://")

        mock_connect.side_effect = Exception("General error")
        result = await command_websocket()
        self.assertFalse(result)
