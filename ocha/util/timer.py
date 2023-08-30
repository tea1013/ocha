import time

from ocha.common.logger import Logger, StdoutLogger


class Timer:
    start_time: float = 0.0
    end_time: float = 0.0
    logger: Logger = StdoutLogger()

    def start(self) -> None:
        self.start_time = time.time()

    def end(self) -> None:
        if self.start_time == 0.0:
            self.logger.error("Timer.start has not been done.")
            return

        self.end_time = time.time()

    @property
    def result(self) -> float:
        if self.end_time == 0.0:
            self.logger.error("Timer.end() has not been done.")
            return 0.0

        return self.end_time - self.start_time
