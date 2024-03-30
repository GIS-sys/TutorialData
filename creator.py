import openpyxl
import random
import string


class Creator:
    @staticmethod
    def xlsx(data, filename="data.xlsx"):
        wb = openpyxl.Workbook()
        sheet = wb.active
        for row, line in enumerate(data):
            for col, cell in enumerate(line):
                sheet.cell(row=row+1, column=col+1, value=cell)
        wb.save(filename)

    @staticmethod
    def csv(data, filename="data.csv", separator=","):
        with open(filename, "w") as f:
            for row, line in enumerate(data):
                for col, cell in enumerate(line):
                    f.write(str(cell))
                    if col != len(line) - 1:
                        f.write(separator)
                f.write("\n")
