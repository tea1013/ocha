from numpy import ndarray
from pandas import DataFrame

from ocha.dataset.cross_validator import CrossValidator


class Dataset:
    def __init__(
        self,
        train_X: DataFrame,
        train_y: DataFrame,
        test_X: DataFrame | None,
        cross_validator: CrossValidator | None,
        categorical_features: list[str] | None,
    ) -> None:
        self.train_X = train_X
        self.train_y = train_y
        self.test_X = test_X
        self.cross_validator = cross_validator
        self.categorical_features = categorical_features

    def fold_index(self, fold: int) -> tuple[ndarray, ndarray]:
        return self.cross_validator.fold_index(fold)
