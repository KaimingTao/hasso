# TODO: may be us yaml to config
#   default.yaml
# config_path = Path(__file__).parent / 'converter.yml'

# for mode, c_names in load_yaml(config_path).items():
#     if mode == 'load':
#         DEFAULT_LOAD_CONVERTERS = [
#             [
#                 i
#                 for i in CONVERTER_LIST
#                 if i.name in c_names
#             ][0]
#             for c in c_names
#         ]
#     else:
#         DEFAULT_DUMP_CONVERTERS = [
#             [
#                 i
#                 for i in CONVERTER_LIST
#                 if i.name in c_names
#             ][0]
#             for c in c_names
#         ]

from .converters import CONVERTERS
from .levels import ConverterList


DEFAULT_LOAD_CONVERTERS = [
    'trim_string_by_cell',
    'remove_blank_row',
    'to_integer_cell',
]
default_load = ConverterList()
for i in DEFAULT_LOAD_CONVERTERS:
    default_load.append(CONVERTERS[i])


DEFAULT_DUMP_CONVERTERS = [
    'trim_string_by_cell',
    'remove_blank_row',
    'to_null_str',
    'boolean_to_str',
    'replace_excel_return',
]
default_dump = ConverterList()
for i in DEFAULT_DUMP_CONVERTERS:
    default_dump.append(CONVERTERS[i])
