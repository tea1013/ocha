from abc import ABC, abstractmethod

from numpy import ndarray
from pandas.core.frame import DataFrame

from ocha.experiment.context import Context
from ocha.experiment.results import ExperimentResult, TestResult, TrainResult, ValidResult
from ocha.models.metrics import Metrics
from ocha.models.model_config import ModelConfig
from ocha.models.model_wrapper import ModelWrapper
from ocha.util.logger import FileLogger, StdoutLogger
from ocha.util.notification import Notification


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

    def __init__(
        self,
        exp_name: str,
        version: int,
        n_fold: int,
        seed: int,
        scoring: Metrics,
        file_logger: FileLogger,
        std_logger: StdoutLogger,
        notification: Notification,
        is_debug: bool = False,
    ) -> None:
        self.exp_name = exp_name
        self.version = version
        self.n_fold = n_fold
        self.seed = seed
        self.scoring = scoring
        self.file_logger = file_logger
        self.std_logger = std_logger
        self.notification = notification
        self.is_debug = is_debug


class Experiment(ABC):
    def __init__(
        self,
        context: Context,
        config: ExperimentConfig,
        folds: list[int],
    ) -> None:
        self.context = context
        self.config = config
        self.folds = folds

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
