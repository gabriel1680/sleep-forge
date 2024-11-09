import os
import time
import pandas as pd
from pathlib import Path


class CsvExporter:

    def export(self, data: dict, filepath: str) -> None:
        data_frame = pd.DataFrame(data)
        filename, timestamp, output_dir = self.__get_path_info(filepath)
        self.create_if_not_exists(output_dir)
        data_frame.to_csv(f"{output_dir}/{timestamp}-{filename}.csv")

    def __get_path_info(self, filepath):
        dirname = os.path.dirname(filepath)
        filename = Path(filepath).stem
        timestamp = int(time.time())
        output_dir = f"{dirname}/dump"
        return filename, timestamp, output_dir

    def create_if_not_exists(self, output_dir):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
