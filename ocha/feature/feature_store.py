import os
import traceback
from enum import Enum
from functools import wraps
from typing import Callable

import pandas as pd
from pandas import DataFrame


class StoreMode(Enum):
    Train = "train"
    Test = "test"


class FeatureStore:
    def __init__(
        self,
        target_df: DataFrame,
        mode: StoreMode,
        save_dir_base: str | None = None,
    ) -> None:
        self.target_df = target_df
        self.mode = mode
        self.save_dir_base = save_dir_base

    @property
    def save_feature(self) -> bool:
        return self.save_dir_base is not None

    @property
    def save_dir(self) -> str:
        return f"{self.save_dir_base}/{self.mode.value}"


def feature(feat_id: str, feature_name: str) -> Callable:
    def _feature(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: list[FeatureStore]) -> DataFrame:
            store = args[0]

            assert isinstance(store, FeatureStore), "args[0] type must be FeatureStore."

            try:
                feats = func(store)
                if store.save_feature:
                    save_feature(feats, feat_id, feature_name, store.save_dir)

                return feats

            except Exception:
                raise Exception(f"exception occured in feature {feature_name}:" f"{traceback.format_exc()}")

        return wrapper

    return _feature


def save_feature(feats: dict | DataFrame, feat_id: str, feature_name: str, dir: str) -> None:
    os.makedirs(dir, exist_ok=True)

    path = os.path.join(dir, f"{feat_id}_{feature_name}.f")

    if isinstance(feats, DataFrame):
        feats.to_feather(path)
    else:
        df = DataFrame.from_dict(feats)
        df.to_feather(path)


def load_feature(store: FeatureStore, feat_id: str, feature_name: str) -> DataFrame:
    path = os.path.join(f"{store.save_dir}/feature", f"{feat_id}_{feature_name}.f")

    return pd.read_feather(path)
