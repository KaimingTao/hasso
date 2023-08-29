class Converter:

    TYPE = None

    def __init__(self, name, asserter, converter):
        self.name = name
        self.asserter = asserter
        self.converter = converter

    def __str__(self):

        return f'{self.__class__}({self.name})'


class ConverterList(list):

    def reinit(self):

        if len(self) > 0:
            self.pop()


class CellConverter(Converter):

    TYPE = 'cell'

    def __call__(self, table):
        new_table = []

        for rec in table:
            for k, v in rec.items():
                if self.asserter(v):
                    rec[k] = self.converter(v)

            new_table.append(rec)

        return new_table


class RowConverter(Converter):

    TYPE = 'row'

    def __call__(self, table):
        new_table = []
        for rec in table:

            if self.asserter(rec):
                rec = self.converter(rec)
            if not rec:
                continue

            new_table.append(rec)
        return new_table


class ColumnConverter(Converter):

    TYPE = 'col'

    def __call__(self, table, column_name):
        new_table = []
        for rec in table:
            val = rec[column_name]
            if self.asserter(val):
                rec[column_name] = self.converter(val)
            new_table.append(rec)

        return new_table


class TableConverter(Converter):

    TYPE = 'table'

    def __call__(self, table):
        return self.converter(table)


# TODo
# use function to collect all local converter
# the convert function can't be a configurable yaml obj, that's the limit.
# definitely for some, need an assert
