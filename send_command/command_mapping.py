class CommandMapping:
    def __init__(self, command: str):
        self.command = command

    def __call__(self, mapping_config: dict) -> None:
        for variable, value in mapping_config.items():
            setattr(self, variable, value)

    def get_command_sequence(self) -> str:
        variables = self.__dict__.items()
        variables = list(filter(lambda x: x[0] not in ["command", "function"], variables))
        variables = [str(v) for k, v in variables]
        return ",".join(variables) + ";"

    def __str__(self) -> str:
        lines = [f"{k}: {v}" for k, v in self.__dict__.items()]
        return "\n".join(lines)
