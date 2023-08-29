import csv
from .argument import check_argument
from .converter.func import convert_table


@convert_table
@check_argument
def dump_csv(file_path, table, header=[]):
    with open(file_path, 'w', encoding='utf-8-sig') as fd:
        writer = csv.DictWriter(fd, fieldnames=header)
        writer.writeheader()
        writer.writerows(table)
