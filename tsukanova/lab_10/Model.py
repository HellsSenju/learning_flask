class Model:
    def __init__(self, name: str, a: int, b: int, c: int):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.set = {}

    def get_props(self) -> list:
        return [self.a, self.b, self.c]


