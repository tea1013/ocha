from abc import ABC, abstractmethod

from pandas import DataFrame

from ocha.dataset.cross_validator import CrossValidator
from ocha.dataset.dataset import Dataset


class DatasetMaker(ABC):
    def __init__(
        self,
        train_X: DataFrame,
        train_y: DataFrame,
        test_X: DataFrame | None,
        cross_validator: CrossValidator | None,
        features: list[str] | None,
    ) -> None:
        self.train_X = train_X
        self.train_y = train_y
        self.test_X = test_X
        self.cross_validator = cross_validator
        self.features = features

    @abstractmethod
    def make(self) -> Dataset:
        pass

    @abstractmethod
    def scaling(self) -> None:
        pass
