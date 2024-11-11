class CommandMapping:
    def __init__(self, command: str):
        self.command = command

    def __call__(self, mapping_config: dict) -> None:
        if not isinstance(mapping_config, dict):
            raise Exception("Wrong input type")
        for variable, value in mapping_config.items():
            setattr(self, variable, value)

    def __str__(self) -> str:
        return f"attributes={self.__dict__})"
