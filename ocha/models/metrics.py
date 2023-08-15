from abc import ABC, abstractmethod

from numpy import ndarray
from pydantic import BaseModel


class Metrics(ABC, BaseModel):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def execute(self, y_true: ndarray, y_pred: ndarray) -> float:
        pass
