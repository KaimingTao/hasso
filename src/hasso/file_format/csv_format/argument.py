from functools import wraps
from pathlib import Path
from .func_mode import get_func_mode
import warnings


def check_argument(func):

    @wraps(func)
    def pack(*args, **kwargs):

        func_mode = get_func_mode(func)

        # TODO get assigned by name, using functools to inspect
        # TODO: use some tricks to speed up the process
        args = list(args)

        args = check_path(args, func_mode)
        args = check_table(args, func_mode)
        kwargs = check_header(args, kwargs, func_mode)

        return func(*args, **kwargs)

    return pack


def check_table(args, func_mode):

    if func_mode != 'dump':
        return args

    file_path = args[0]
    table = args[1]
    if not table:
        warnings.warn(f'{file_path} table is empty.')

    return args


def check_header(args, kwargs, func_mode):
    if func_mode != 'dump':
        return kwargs

    # use kw dict to pass args and kwargs in check functions
    table = args[1]
    header = kwargs.get('header')

    if header:
        return kwargs

    header = []
    for rec in table:
        for key in rec.keys():
            if key not in header:
                header.append(key)

    kwargs['header'] = header

    return kwargs


# TODO: get table columns by header, using the partial info and using table converter
# def dump_csv(file_path, table, headers=[], remain=True):

#     table_headers = []
#     for rec in table:
#         for key in rec.keys():
#             if key not in table_headers:
#                 table_headers.append(key)

#     if not headers:
#         headers = table_headers
#     else:
#         remain_headers = [
#             i
#             for i in table_headers
#             if i not in headers
#         ]
#         if remain:
#             headers = headers + remain_headers
#         table = [
#             {
#                 k: v
#                 for k, v in i.items()
#                 if k in headers
#             }
#             for i in table
#         ]

#     with open(file_path, 'w', encoding='utf-8-sig') as fd:
#         writer = csv.DictWriter(fd, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(table)


def check_path(args, func_mode):

    file_path = args[0]

    if type(file_path) == str:
        file_path = Path(file_path).expanduser().resolve()

    if func_mode == 'load':
        # TODO: load file default two ways,
        #   1 raise exception,
        #   2 warning return []
        # implement a switch
        if not file_path.exists():
            raise Exception(f'{file_path} not found')
    else:
        # TODO: help use make folder or not
        file_path.parent.mkdir(exist_ok=True, parents=True)

    args[0] = file_path

    return args
