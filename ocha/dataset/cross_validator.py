from pandas import DataFrame
from pandas.core.indexes.base import Index


class CrossValidator:
    def __init__(self, folds: DataFrame) -> None:
        self.folds = folds

    def fold_index(self, fold: int) -> tuple[Index, Index]:
        train_idx = self.folds[self.folds["fold"] != fold].index
        valid_idx = self.folds[self.folds["fold"] == fold].index

        return train_idx, valid_idx
