from ocha.config.version import Version
from ocha.util.logger import FileLogger, StdoutLogger
from ocha.util.notification import Notification


class GlobalConfig:
    version: Version
    logger: StdoutLogger
    file_logger: FileLogger
    notification: Notification
    n_fold: int
    seed: int
    optimize: bool
    debug: bool
    is_local: bool
    remake: bool = False

    def __init__(
        self,
        version: Version,
        logger: StdoutLogger,
        file_logger: FileLogger,
        notification: Notification,
        n_fold: int,
        seed: int,
        optimize: bool,
        debug: bool,
        is_local: bool,
        remake: bool = False,
    ) -> None:
        self.version = version
        self.logger = logger
        self.file_logger = file_logger
        self.notification = notification
        self.n_fold = n_fold
        self.seed = seed
        self.optimize = optimize
        self.debug = debug
        self.is_local = is_local
        self.remake = remake

        if not self.debug:
            self.file_logger.default(
                [
                    "",
                    "",
                    "============================================",
                    f"version: {version.n}",
                    "============================================",
                    "",
                    "",
                ]
            )

        self.notification.notify(f"Experiment [v{version.n}] Start.")
