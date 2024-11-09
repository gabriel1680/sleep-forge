from typing import Protocol


class Calculator(Protocol):
    def calculate(self, filename: str) -> dict:
        ...


class DirectoryScanner(Protocol):
    def scan_dir(self, dirname: str) -> list[str]:
        ...


class DataExporter(Protocol):
    def export(self, data: dict, filepath: str) -> dict:
        ...


class GenerateCalculatedCsvFilesUseCase:

    def __init__(self, scanner: DirectoryScanner, calculator: Calculator, exporter: DataExporter) -> None:
        self.scanner = scanner
        self.calculator = calculator
        self.exporter = exporter

    def execute(self, selected_dir: str) -> None:
        results = []
        for filepath in self.scanner.scan_dir(selected_dir):
            data = self.calculator.calculate(filepath)
            results.append(data)

        data_result = {'DeviceID': [],
                'SubjectName': [],
                'IS': [],
                'ISM': [],
                'ISp': [],
                'IV': [],
                'IVm': [],
                'IVp': [],
                'L5': [],
                'L5p': [],
                'M10': [],
                'M10p': [],
                'PIM': [],
                'PIMn': [],
                'RA': [],
                'RAp': [],
                'SleepMidPoint': [],
                'SleepProfile': [],
                'SleepRegulatoryIndex': [],
                'SoD': [],
                'amb_light': [],
                'average_daily_activity': [],
                # 'average_daily_light': [],
                'blue_light': [],
                'ir_light': [],
                'light': [],
                'temperature': [],
                'white_light': [],
                'Roenneberg': [],
                'Roenneberg_AoT': [],
                # 'Crespo': [],
                # 'Crespo_AoT': [],
               }

        for result in results:
            for key, value in result.items():
                data_result[key].append(value)

        self.exporter.export(data_result, f"{selected_dir}/dump.txt")

