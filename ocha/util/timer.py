import time


class Timer:
    start_time: float = 0.0
    end_time: float = 0.0

    def start(self) -> None:
        self.start_time = time.time()

    def end(self) -> None:
        if self.start_time == 0.0:
            print("Timer.start has not been done.")

        self.end_time = time.time()

    @property
    def result(self) -> float:
        if self.end_time == 0.0:
            print("Timer.end() has not been done.")

        return self.end_time - self.start_time
