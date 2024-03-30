import openpyxl
import random
import string

from pathlib import Path


class Creator:
    @staticmethod
    def folder(folder):
        Path(folder).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_folder_name(path):
        return Path(path).parent

    @staticmethod
    def xlsx(data, filename="data/data.xlsx"):
        Creator.folder(Creator.get_folder_name(filename))
        wb = openpyxl.Workbook()
        sheet = wb.active
        for row, line in enumerate(data):
            for col, cell in enumerate(line):
                sheet.cell(row=row+1, column=col+1, value=cell)
        wb.save(filename)

    @staticmethod
    def csv(data, filename="data/data.csv", separator=","):
        Creator.folder(Creator.get_folder_name(filename))
        with open(filename, "w") as f:
            for row, line in enumerate(data):
                for col, cell in enumerate(line):
                    f.write(str(cell))
                    if col != len(line) - 1:
                        f.write(separator)
                f.write("\n")
