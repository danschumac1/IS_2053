import csv


def read_csv_file(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv_file(file_path: str, data: list):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def append_csv_file(file_path: str, data: list):
    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
