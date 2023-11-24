from abc import ABC, abstractmethod

from numpy import ndarray
from pandas import DataFrame

from ocha.common.base_model import BaseModel


class Context(ABC, BaseModel):
    train: DataFrame
    test: DataFrame | None
    sample_oof_df: DataFrame | None
    sample_submission_df: DataFrame | None

    @abstractmethod
    def make_oof(self, oof_prediction: ndarray) -> DataFrame:
        pass

    @abstractmethod
    def make_submission(self, test_prediction: ndarray) -> DataFrame:
        pass

    def update_sample_submission_df(self, new_sample_submission_df: DataFrame) -> None:
        self.sample_submission_df = new_sample_submission_df
