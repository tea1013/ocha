from abc import ABC, abstractmethod
from typing import Any

from pandas import DataFrame
from ocha.common.base_model import BaseModel


class Preprocess(ABC, BaseModel):
    source: DataFrame
    source_processed: DataFrame | None = None
    preprocessing_objects: dict[str, Any] | None = None

    @abstractmethod
    def preprocess(self) -> None:
        pass

    def get_procesed(self) -> DataFrame | None:
        return self.source_processed

    def get_preprocessing_objects(self) -> dict[str, Any] | None:
        return self.preprocessing_objects
