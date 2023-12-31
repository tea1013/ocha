from abc import ABC, abstractmethod

from pandas import DataFrame

from ocha.common.base_model import BaseModel


class Dataset(ABC, BaseModel):
    train: DataFrame
    valid: DataFrame
    test: DataFrame

    @property
    @abstractmethod
    def all_features(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def categorical_features(self) -> list[str]:
        pass

    @property
    def continuous_features(self) -> list[str]:
        result = []
        for col in self.all_features:
            if col not in self.categorical_features:
                result.append(col)

        return result

    @property
    @abstractmethod
    def targets(self) -> list[str]:
        pass

    @abstractmethod
    def processing_train(self) -> None:
        pass

    @abstractmethod
    def processing_valid(self) -> None:
        pass

    @abstractmethod
    def processing_test(self) -> None:
        pass
