from pydantic import BaseModel


class Version(BaseModel):
    n: int

    def __init__(self, n: int) -> None:
        self.n = n
