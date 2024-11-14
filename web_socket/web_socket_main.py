import asyncio

import websockets


class WebSocketMain:
    def __init__(self, command_sequence: str, web_socket_output: str, timeout: float = 1.0):
        self.command_sequence = command_sequence
        self.web_socket_output = 'ws://' + web_socket_output
        self.timeout = timeout

    async def __call__(self) -> any:
        try:
            async with await websockets.connect(self.web_socket_output) as websocket:
                await websocket.send(self.command_sequence)
                print(f"sent: {self.command_sequence}")
                response = await asyncio.wait_for(websocket.recv(), timeout=self.timeout)
                return response
        except asyncio.TimeoutError:
            print("command correctly received")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
