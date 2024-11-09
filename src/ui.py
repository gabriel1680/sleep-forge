import os
import queue
import threading
import tkinter as tk
import tkinter.filedialog as dialog
from generate_csv_files_usecase import GenerateCalculatedCsvFilesUseCase


class UI(tk.Tk):

    def __init__(self, use_case: GenerateCalculatedCsvFilesUseCase) -> None:
        super().__init__()
        self.queue = queue.Queue()
        self.title('Actigraphy Data Calculator')
        self.geometry('500x300')
        self.selected_dir = ""
        self.use_case = use_case
        self.bind("<<CalculationFinished>>",
                  lambda _: self.on_end_processing())
        self.create_ui()

    def create_ui(self) -> None:
        self.frame = tk.Frame(self, padx=16, pady=16)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, font=(
            "Arial", 20), text="Select a folder which have the generated .txt condor files", pady=32, wraplength=375)
        self.label.pack(side=tk.TOP)

        self.filepath = tk.Label(self.frame, font=("Arial", 14), pady=32)

        self.calculate_btn = tk.Button(self.frame, font=(
            "Arial", 16), text="calculate", pady=16, padx=16, borderwidth=0, command=self.handle_calculate)

        self.select_file_btn = tk.Button(self.frame, font=(
            "Arial", 16), text="choose a folder", pady=16, padx=16, borderwidth=0, command=self.handle_click)
        self.select_file_btn.pack(anchor=tk.CENTER)

    def handle_click(self) -> None:
        directory = dialog.askdirectory()
        if directory == "":
            return
        self.selected_dir = directory
        self.filepath["text"] = directory
        self.label.pack_forget()
        self.filepath.pack(anchor=tk.NE)
        self.select_file_btn.pack_forget()
        self.calculate_btn.pack(anchor=tk.CENTER)

    def handle_calculate(self) -> None:
        self.set_loading_state()
        threading.Thread(
            target=self.execute, args=(self.selected_dir, ),
            daemon=True).start()

    def set_loading_state(self) -> None:
        self.calculate_btn["text"] = "calculating..."
        self.calculate_btn["state"] = "disabled"

    def execute(self, selected_dir: str):
        self.use_case.execute(selected_dir)
        self.event_generate("<<CalculationFinished>>")

    def set_select_folder_state(self) -> None:
        self.calculate_btn["text"] = "calculate"
        self.calculate_btn["state"] = "active"
        self.label.pack(side=tk.TOP)
        self.filepath.pack_forget()
        self.select_file_btn.pack(anchor=tk.CENTER)
        self.calculate_btn.pack_forget()

    def on_end_processing(self) -> None:
        self.set_select_folder_state()
        os.system(f"open {self.selected_dir}")
