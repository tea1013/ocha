from abc import ABC, abstractmethod

from numpy import ndarray
from pandas.core.frame import DataFrame

from ocha.common.base_model import BaseModel
from ocha.dataset.cross_validator import CrossValidator
from ocha.experiment.context import Context
from ocha.experiment.results import ExperimentResult, TestResult, TrainResult, ValidResult
from ocha.models.metrics import Metrics
from ocha.models.model_config import ModelConfig
from ocha.models.model_wrapper import ModelWrapper


class ExperimentConfig(BaseModel):
    version: int
    n_fold: int
    seed: int
    scoring: Metrics
    cross_validator: CrossValidator
    folds: list[int] | None = None


class Experiment(ABC, BaseModel):
    context: Context
    config: ExperimentConfig

    def get_folds(self) -> list[int]:
        if self.config.folds is None:
            return [i for i in range(self.config.n_fold)]
        else:
            return self.config.folds

    @abstractmethod
    def build_conf(self, fold: int | None) -> ModelConfig:
        pass

    @abstractmethod
    def build_model(self, conf: ModelConfig) -> ModelWrapper:
        pass

    @abstractmethod
    def run(self) -> ExperimentResult:
        pass

    @abstractmethod
    def train(self) -> TrainResult:
        pass

    @abstractmethod
    def valid(self) -> ValidResult:
        pass

    @abstractmethod
    def test(self) -> TestResult:
        pass

    @abstractmethod
    def test_seq(self, test_X: DataFrame | ndarray) -> TestResult:
        # Time-Series APIコンペ用
        pass

    @abstractmethod
    def optimize(self) -> None:
        pass

    @abstractmethod
    def save_oof(self, oof_prediction: ndarray, score: float) -> DataFrame:
        pass

    @abstractmethod
    def save_submission(self, test_prediction: ndarray, score: float) -> DataFrame:
        pass

    @abstractmethod
    def remake(self) -> None:
        pass
