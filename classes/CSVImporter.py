import pandas as pd
import os
from configs.csv_config import csv_config


class CSVImporter:

    def __init__(self):
        self._csv_config = csv_config
        print("CSV Importer instantiated")

    def get_historic_data(self, path: str = None) -> pd.DataFrame:
        """
        Pulls the data specified in the config, or otherwise specified

        :param path: optionally specify a different path to a historic csv file, pulled from yahoo finance
        :return: a data frame object of the csv
        """

        if not path:
            path = self._csv_config["PATH_TO_HISTORIC_DATA"]

        df = self.read_csv(path)

        return df

    def read_csv(self, path: str) -> pd.DataFrame:
        """
        Generic wrapper for pd.read_csv, does a quick check for presence

        :param path: the path to a file to import
        :return: a dataframe of the file
        """

        if self._check_for_a_file(path):
            df = pd.read_csv(path)

        else:
            raise ValueError(f"{path} does not exist... can't import csv")

        return df

    @staticmethod
    def _check_for_a_file(path: str) -> bool:

        return os.path.exists(path)

