from __future__ import annotations

from abc import ABC, abstractmethod

from numpy import ndarray
from pandas import DataFrame, Series

from ocha.common.base_model import BaseModel
from ocha.models.metrics import Metrics
from ocha.models.model_config import ModelConfig


class FitResult(BaseModel):
    model: ModelWrapper
    oof_prediction: ndarray
    score: float


FitResults = list[FitResult]


class ModelWrapper(ABC):
    config: ModelConfig
    scoring: Metrics

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
