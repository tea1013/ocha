from numpy import ndarray
from pandas import DataFrame

from ocha.dataset.cross_validator import CrossValidator


class Dataset:
    def __init__(
        self,
        train_X: DataFrame,
        train_y: DataFrame,
        test_X: DataFrame | None,
        categorical_features: list[str] | None,
    ) -> None:
        self.train_X = train_X
        self.train_y = train_y
        self.test_X = test_X
        self.categorical_features = categorical_features
