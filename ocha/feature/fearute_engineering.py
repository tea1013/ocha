from typing import Callable

import pandas as pd
from pandas import DataFrame

from ocha.feature.feature_store import FeatureStore


class FeatureEngineering:
    def __init__(self, store: FeatureStore, fs: list[Callable]) -> None:
        self.store = store
        self.fs = fs

    def transform(self, debug: bool = False) -> DataFrame:
        features = []
        for f in self.fs:
            if debug:
                print(f.__name__)
            d = f(self.store)
            feature = pd.DataFrame().from_dict(d)
            features.append(feature)

        result = pd.concat(features, axis=1)

        if debug:
            print("Finish!")

        return result
