from abc import ABC, abstractmethod

from numpy import ndarray

from ocha.experiment.experiment import Experiment


class Ensemble(ABC):
    @abstractmethod
    def ensemble(self, experiments: list[Experiment]) -> ndarray:
        pass
