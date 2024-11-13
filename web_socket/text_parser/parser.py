from text_parser.message import Message


class Parser:
    def __init__(self, concatenated_text: str, upper_length: int):
        self.upper_length = upper_length
        self.input_command = self._pre_process_input(concatenated_text)

    def _pre_process_input(self, text) -> list:
        if not self._check_input(text):
            raise ValueError("wrong input length")
        return text.split(',')

    def _check_input(self, text) -> bool:
        if len(text.split(",")) == self.upper_length:
            return True
        return False

    def __call__(self, variables: dict) -> None:
        for i, (name, function) in enumerate(variables.items()):
            general_message = Message(name, function, self.input_command[i])
            setattr(self, name, general_message)

    def __str__(self):
        parser_vars = {
            k: v for k, v in self.__dict__.items()
            if k not in ['upper_length', 'input_command']
        }
        return '\n'.join(str(message_value) for message_value in parser_vars.values())
