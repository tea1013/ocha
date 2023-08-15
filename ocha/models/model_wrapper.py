from __future__ import annotations

from abc import ABC, abstractmethod

from numpy import ndarray
from pandas import DataFrame, Series

from ocha.models.metrics import Metrics
from ocha.models.model_config import ModelConfig
from ocha.util.logger import FileLogger, StdoutLogger


class FitResult:
    model: ModelWrapper
    oof_prediction: ndarray
    score: float


class ModelWrapper(ABC):
    def __init__(
        self,
        config: ModelConfig,
        scoring: Metrics,
        file_logger: FileLogger,
        std_logger: StdoutLogger,
    ) -> None:
        self.config = config
        self.scoring = scoring
        self.file_logger = file_logger
        self.std_logger = std_logger

    @abstractmethod
    def build(self) -> None:
        pass

    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def fit(
        self,
        X_train: DataFrame | ndarray,
        y_train: Series | ndarray,
        X_valid: DataFrame | ndarray,
        y_valid: Series | ndarray,
    ) -> FitResult:
        pass

    @abstractmethod
    def predict(self, X_test: DataFrame | ndarray) -> ndarray:
        pass

    @abstractmethod
    def save(self) -> None:
        pass
