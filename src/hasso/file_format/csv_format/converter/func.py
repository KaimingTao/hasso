from functools import wraps
from ..func_mode import get_func_mode
from .converters import CONVERTERS
from .default import default_load
from .default import default_dump


def convert_table(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        mode = get_func_mode(func)

        if mode == 'load':
            converters = kwargs.pop('converters', default_load)

            table = func(*args, **kwargs)

            table = apply_converters(table, converters)

            return table

        elif mode == 'dump':
            converters = kwargs.pop('converters', default_dump)

            # TODO, maybe check which position contains the table in parameter
            table = args[1]
            table = apply_converters(table, converters)

            args = list(args)
            args[1] = table

            return func(*args, **kwargs)

    return wrapper


def apply_converters(table, converters):

    # print(converters)
    for c in converters:
        arg = None
        if type(c) == list:
            c, arg = c
        if type(c) == str:
            c = CONVERTERS.get(c)

        if not c:
            raise Exception(f'Converter {c} not found')

        if arg:
            table = c(table, arg)
        else:
            table = c(table)

    return table
