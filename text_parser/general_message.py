class GeneralMessage:
    def __init__(self, name: str, function: str, value: int):
        self.name = name
        self.function = function
        self.value = int(value)

    def __eq__(self, other):
        return self.name == other.name and self.function == other.function and self.value == other.value

    def __str__(self):
        return f"name = {self.name}, value = {self.value}"
