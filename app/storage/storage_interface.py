from abc import ABC, abstractmethod

import pandas as pd


class StorageInterface(ABC):

    @abstractmethod
    def write(
        self,
        dataframe: pd.DataFrame,
        layer: str,
        partition:str,
        filename: str,
    ):
        pass