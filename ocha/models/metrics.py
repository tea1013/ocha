from abc import ABC, abstractmethod

from numpy import ndarray


class Metrics(ABC):
    name: str

    @abstractmethod
    def execute(self, y_true: ndarray, y_pred: ndarray) -> float:
        pass
