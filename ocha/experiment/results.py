from numpy import ndarray
from pandas import DataFrame

from ocha.models.model_wrapper import FitResult


class TrainResult:
    fit_results: list[FitResult]
    oof_prediction: ndarray
    score: float


class ValidResult:
    oof_prediction: ndarray
    score: float


class TestResult:
    test_prediction: ndarray


TrainResults = list[TrainResult]

TestResults = list[TestResult]


class ExperimentResult:
    fit_results: list[FitResult] | None
    oof_prediction: ndarray
    test_prediction: ndarray
    oof_df: DataFrame
    submission_df: DataFrame
    score: float
    time: float


class RemakeResult:
    oof_df: DataFrame
    submission_df: DataFrame
    score: float
