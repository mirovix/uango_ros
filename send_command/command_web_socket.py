import websockets


class CommandWebSocket:
    def __init__(self, command_sequence: str, web_socket_output: str = "ws://192.168.12.1:8080"):
        self.command_sequence = command_sequence
        self.web_socket_output = web_socket_output

    async def __call__(self) -> bool:
        try:
            async with await websockets.connect(self.web_socket_output) as websocket:
                await websocket.send(self.command_sequence)
                print(f"sent: {self.command_sequence}")

                await websocket.recv()
                print(f"command correctly received")
                return True

        except Exception as e:
            print(f"An error occurred: {e}")
        return False
