import tkinter as tk

from uango_connector.main import WebSocketApp


class ControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Uango Control")
        self.root.geometry("1715x1150")

    def __call__(self) -> None:
        for index, button in enumerate(self.get_buttons_name()):
            self._get_button(button, index // 3, index % 3)

    def _get_button(self, text, row, column) -> None:
        label = text.upper().replace("_", " ")
        command = WebSocketApp(text)
        button = tk.Button(self.root, text=label, command=command.run)
        button.config(height=6, width=30)
        button.grid(row=row, column=column, padx=10, pady=10)

    @staticmethod
    def get_buttons_name() -> list[str]:
        return [
            "turn_on",
            "homing_up",
            "reset_fault",
            "first_step_jerk_dx",
            "first_step_jerk_sx",
            "first_step_jerk_walk_dx",
            "first_step_jerk_walk_sx",
            "first_step_invp_dx",
            "first_step_invp_sx",
            "first_step_invp_walk_dx",
            "first_step_invp_walk_sx",
            "next",
            "stop",
            "get_stream"
        ]
