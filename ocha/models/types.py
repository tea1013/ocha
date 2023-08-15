from numpy import ndarray

from ocha.models.model_wrapper import ModelWrapper


class FitResult:
    model: ModelWrapper
    oof_prediction: ndarray
    score: float
