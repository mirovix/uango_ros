import asyncio
import unittest
from unittest.mock import AsyncMock, patch

from web_socket.web_socket_main import WebSocketMain


class TestCommandWebSocket(unittest.IsolatedAsyncioTestCase):
    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenCommandSequence_whenCallingCommandWebSocket_thenReturnTrue(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = WebSocketMain(command_sequence, "ws://")

        mock_websocket = AsyncMock()
        mock_connect.return_value = mock_websocket

        result = await command_websocket()
        self.assertTrue(result)

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenWrongWebSocketOutput_whenCallingCommandWebSocket_thenReturnNone(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = WebSocketMain(command_sequence, "ws://")

        mock_connect.side_effect = Exception("General error")
        result = await command_websocket()
        self.assertIsNone(result)

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenTimeoutError_whenCallingCommandWebSocket_thenReturnNone(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = WebSocketMain(command_sequence, "ws://", 0.0)

        mock_websocket = AsyncMock()
        mock_websocket.recv.side_effect = asyncio.TimeoutError
        mock_connect.return_value = mock_websocket

        result = await command_websocket()
        self.assertIsNone(result)
