import pandas as np
import os.path
from datetime import datetime as dt
from pathlib import Path
import logging
import os


class IncreaseProfitSixthCampaign():
    def __init__(self):
        self.path_csv_file = Path(__file__).parent.parent / "ml_project1_data.csv"

    def run(self):
        dataFrame = self.read_csv()
        return True

    def read_csv(self):
        try:
            data = np.read_csv(self.path_csv_file, sep=',', header=0)
            data_columns = data.columns()
            if data.head():
                print(data.describe())
                return True
            else:
                print("File empty!")

        except Exception:
            print("")


def main():
    IncreaseProfitSixthCampaign().run()


if __name__ == "__main__":
    main()
