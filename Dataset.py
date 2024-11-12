import os
import pyreadr


class Dataset:
    def __init__(self, data_path: str = "./data") -> None:
        self.datasets = dict()
        for file in os.listdir(data_path):
            name = file.split(".")[0]
            self.datasets[name.split(".")[0]] = pyreadr.read_r(
                os.path.join(data_path, file)
            )[name]

        self.datasets["cancer"] = [
            124,
            42,
            25,
            45,
            412,
            51,
            1112,
            46,
            103,
            876,
            146,
            340,
            396,
        ]  # dataframes with more than 3 columns are not supported by pyreadr

    def __getattr__(self, name: str):
        if name in self.datasets.keys():
            return self.datasets[name]
        return object.__getattribute__(self, name)
