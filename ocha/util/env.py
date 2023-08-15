import sys


def in_colab() -> bool:
    return "google.colab" in sys.modules


def in_kaggle() -> bool:
    return "kaggle_web_client" in sys.modules


def in_local() -> bool:
    return not (in_colab() or in_kaggle())
