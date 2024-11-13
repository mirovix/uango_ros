import os

import yaml

from web_socket.send_command.command_mapping import CommandMapping


class CommandMain:
    def __init__(self, args: list):
        self.command = self._check_command(args)
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.yaml_path = os.path.join(base_path, "mapping.yaml")

    @staticmethod
    def _check_command(args: list) -> str:
        if len(args) < 2:
            print("Empty command")
            exit(1)
        return args[1]

    def __call__(self):
        yaml_map = self._load_mapping_yaml()
        self._check_input_command(yaml_map)
        return self._create_command_mapping(self.command, yaml_map[self.command])

    def _check_input_command(self, mapping: dict) -> None:
        if self.command not in mapping:
            print(f"Command not found: {self.command}")
            exit(1)

    def _load_mapping_yaml(self) -> dict:
        if not os.path.exists(self.yaml_path):
            raise FileNotFoundError(f"File not found: {self.yaml_path}")

        with open(self.yaml_path) as file:
            mapping = yaml.load(file, Loader=yaml.FullLoader)

        return mapping

    @staticmethod
    def _create_command_mapping(variable: str, value: dict) -> CommandMapping:
        command_mapping = CommandMapping(variable)
        command_mapping(value)
        return command_mapping
