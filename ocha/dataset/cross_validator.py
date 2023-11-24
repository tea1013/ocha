import pandas as pd
from pandas.core.indexes.base import Index

from ocha.common.base_model import BaseModel


class CrossValidator(BaseModel):
    folds: pd.DataFrame

    def fold_index(self, fold: int) -> tuple[Index, Index]:
        train_idx = self.folds[self.folds["fold"] != fold].index
        valid_idx = self.folds[self.folds["fold"] == fold].index

        return train_idx, valid_idx
