from abc import ABC, abstractmethod

from numpy import ndarray
from pandas.core.frame import DataFrame

from ocha.common.logger import FileLogger, StdoutLogger
from ocha.common.notification import Notification
from ocha.experiment.context import Context
from ocha.experiment.results import ExperimentResult, TestResult, TrainResult, ValidResult
from ocha.models.metrics import Metrics
from ocha.models.model_config import ModelConfig
from ocha.models.model_wrapper import ModelWrapper


class ExperimentConfig:
    exp_name: str
    version: int
    n_fold: int
    seed: int
    scoring: Metrics
    file_logger: FileLogger
    std_logger: StdoutLogger
    notification: Notification
    is_debug: bool = False


class Experiment(ABC):
    context: Context
    config: ExperimentConfig
    folds: list[int]

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
