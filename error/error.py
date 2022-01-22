class BlockNotValid(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class UTException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
