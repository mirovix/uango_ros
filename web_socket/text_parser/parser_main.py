import os

import yaml

from text_parser.parser import Parser


class ParserMain:
    def __init__(self, concatenated_text: str):
        self.concatenated_text = concatenated_text.rstrip(';')
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.yaml_path = os.path.join(base_path, "exo_data.yaml")

    def _load_mapping_yaml(self) -> dict:
        if not os.path.exists(self.yaml_path):
            raise FileNotFoundError(f"File not found: {self.yaml_path}")

        with open(self.yaml_path) as file:
            exo_data = yaml.load(file, Loader=yaml.FullLoader)

        return exo_data

    def __call__(self) -> None:
        exo_data = self._load_mapping_yaml()

        self.stream = self._process_parser(0, 12, 12, exo_data['stream'])
        self._map_system_state(exo_data['system_state'])

        self.fem_left = self._process_parser(12, 35, 23, exo_data['joint'])
        self.tib_left = self._process_parser(35, 58, 23, exo_data['joint'])
        self.fem_right = self._process_parser(58, 81, 23, exo_data['joint'])
        self.tib_right = self._process_parser(81, 104, 23, exo_data['joint'])

    def _process_parser(self, start: int, end: int, length: int, exo_data: dict) -> Parser:
        text = ','.join(self.concatenated_text.split(',')[start:end])
        parser = Parser(text, length)
        parser(exo_data)
        return parser

    def _map_system_state(self, exo_data: dict) -> None:
        state = getattr(self.stream, 'system_state').value
        self.stream.__dict__['system_state'].value = exo_data[state]

    def __str__(self) -> str:
        return (f"Stream:\n{self.stream}\n"
                f"\nFemur Left:\n{self.fem_left}\n"
                f"\nTibia Left:\n{self.tib_left}\n"
                f"\nFemur Right:\n{self.fem_right}\n"
                f"\nTibia Right:\n{self.tib_right}")
