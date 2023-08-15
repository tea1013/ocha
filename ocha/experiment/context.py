from abc import ABC, abstractmethod

from numpy import ndarray
from pandas import DataFrame

from ocha.dataset.dataset import Dataset


class Context(ABC):
    def __init__(
        self,
        dataset: Dataset | None,
        sample_oof_df: DataFrame | None,
        sample_submission_df: DataFrame | None,
    ) -> None:
        self.dataset = dataset
        self.sample_oof_df = sample_oof_df
        self.sample_submission_df = sample_submission_df

    @abstractmethod
    def make_oof(self, oof_prediction: ndarray) -> DataFrame:
        pass

    @abstractmethod
    def make_submission(self, test_prediction: ndarray) -> DataFrame:
        pass

    def update_sample_submission_df(self, new_sample_submission_df: DataFrame) -> None:
        self.sample_submission_df = new_sample_submission_df
