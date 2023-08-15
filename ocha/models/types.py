from numpy import ndarray
from pydantic import BaseModel

from ocha.models.model_wrapper import ModelWrapper


class FitResult(BaseModel):
    model: ModelWrapper
    oof_prediction: ndarray
    score: float
