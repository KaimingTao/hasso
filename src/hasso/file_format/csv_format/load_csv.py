import csv
from .argument import check_argument
from .converter.func import convert_table


@convert_table
@check_argument
def load_csv(
        file_path,
        encoding='utf-8-sig'):

    table = []
    with open(file_path, encoding=encoding) as fd:
        for record in csv.DictReader(fd):
            table.append(record)

    return table
