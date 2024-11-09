from ui import UI
from calculator import ActigraphyCalculator
from exporter import CsvExporter
from scanner import OsDirScanner
from generate_csv_files_usecase import GenerateCalculatedCsvFilesUseCase


def main() -> None:
    calculator = ActigraphyCalculator()
    dir_scanner = OsDirScanner()
    exporter = CsvExporter()
    use_case = GenerateCalculatedCsvFilesUseCase(dir_scanner, calculator, exporter)
    application = UI(use_case)
    application.mainloop()


if __name__ == "__main__":
    main()
