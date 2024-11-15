import asyncio
import unittest
from unittest.mock import AsyncMock, patch

from uango_connector.web_socket_connection import WebSocketConnection


class TestCommandWebSocket(unittest.IsolatedAsyncioTestCase):
    @patch('websockets.connect', new_callable=AsyncMock)
    async def test_givenCorrectWebSocketOutput_whenCallingCommandWebSocket_thenReturnResponse(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = WebSocketConnection(command_sequence, "ws://")

        mock_websocket = AsyncMock()
        mock_websocket.recv.return_value = "Response"
        mock_connect.return_value = mock_websocket

        result = await command_websocket()
        self.assertEqual(result, "Response")

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenWrongWebSocketOutput_whenCallingCommandWebSocket_thenReturnNone(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = WebSocketConnection(command_sequence, "ws://")

        mock_connect.side_effect = Exception("General error")
        result = await command_websocket()
        self.assertIsNone(result)

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_givenTimeoutError_whenCallingCommandWebSocket_thenReturnNone(self, mock_connect):
        command_sequence = "20,100;"
        command_websocket = WebSocketConnection(command_sequence, "ws://", 0.0)

        mock_websocket = AsyncMock()
        mock_websocket.recv.side_effect = asyncio.TimeoutError
        mock_connect.return_value = mock_websocket

        result = await command_websocket()
        self.assertIsNone(result)
