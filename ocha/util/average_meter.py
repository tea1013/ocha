from ocha.common.base_model import BaseModel


class AverageMeter(BaseModel):
    val: float = 0.0
    avg: float = 0.0
    sum: float = 0.0
    count: int = 0

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.val = 0.0
        self.avg = 0.0
        self.sum = 0.0
        self.count = 0

    def update(self, val: float, n: int = 1) -> None:
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count
