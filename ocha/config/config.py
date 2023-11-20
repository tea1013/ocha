from common.base_model import BaseModel


class GlobalConfig(BaseModel):
    version: int
    n_fold: int
    seed: int
