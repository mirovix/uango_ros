import asyncio

import websockets


class WebSocketConnection:
    def __init__(self, command_sequence: str, web_socket_output: str, timeout: float = 1.0):
        self.command_sequence = command_sequence
        self.web_socket_output = 'ws://' + web_socket_output
        self.timeout = timeout

    async def __call__(self) -> any:
        websocket = None
        try:
            websocket = await websockets.connect(self.web_socket_output)
            await self._send_command(websocket)
            response = await self._receive_response(websocket)
            return response
        except Exception as e:
            print(f"Error occurred during WebSocket communication: {e}")
            return None
        finally:
            if websocket:
                await websocket.close()

    async def _send_command(self, websocket):
        await websocket.send(self.command_sequence)
        print(f"Command sent: {self.command_sequence}")

    async def _receive_response(self, websocket) -> any:
        try:
            return await asyncio.wait_for(websocket.recv(), timeout=self.timeout)
        except asyncio.TimeoutError:
            return None
