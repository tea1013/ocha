from abc import ABC, abstractmethod

from numpy import ndarray

from ocha.common.base_model import BaseModel


class Metrics(ABC, BaseModel):
    name: str

    @abstractmethod
    def execute(self, y_true: ndarray, y_pred: ndarray) -> float:
        pass
