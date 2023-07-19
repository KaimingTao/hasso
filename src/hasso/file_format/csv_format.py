import csv


def load_csv(
        file_path,
        encoding='utf-8-sig'):

    table = []
    with open(file_path, encoding=encoding) as fd:
        for record in csv.DictReader(fd):
            table.append(record)

    return table


def dump_csv(file_path, table, headers):

    with open(file_path, 'w', encoding='utf-8-sig') as fd:
        writer = csv.DictWriter(fd, fieldnames=headers)
        writer.writeheader()
        writer.writerows(table)



