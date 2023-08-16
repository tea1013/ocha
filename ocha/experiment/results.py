from numpy import ndarray
from pandas import DataFrame
from pydantic import BaseModel

from ocha.models.model_wrapper import FitResults


class TrainResult(BaseModel):
    fit_results: FitResults
    oof_prediction: ndarray
    score: float


class ValidResult(BaseModel):
    oof_prediction: ndarray
    score: float


class TestResult(BaseModel):
    test_prediction: ndarray


TrainResults = list[TrainResult]

TestResults = list[TestResult]


class ExperimentResult(BaseModel):
    fit_results: FitResults | None
    oof_prediction: ndarray
    test_prediction: ndarray
    oof_df: DataFrame
    submission_df: DataFrame
    score: float
    time: float


class RemakeResult(BaseModel):
    oof_df: DataFrame
    submission_df: DataFrame
    score: float
