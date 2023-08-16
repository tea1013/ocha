from abc import ABC, abstractclassmethod
from enum import Enum

from ocha.util.env import in_kaggle

if not in_kaggle():
    import slackweb


class NotificationPlatform(Enum):
    Slack = 0


class Notification(ABC):
    @abstractclassmethod
    def notify(self, body: str) -> None:
        pass


class Stdout(Notification):
    def __init__(self) -> None:
        pass

    def notify(self, body: str) -> None:
        print(body)


class Slack(Notification):
    def __init__(self, url: str) -> None:
        self.slack = slackweb.Slack(url=url)

    def notify(self, body: str) -> None:
        self.slack.notify(text=body)
