from ..levels import CellConverter
from ..levels import RowConverter
from ..levels import ColumnConverter
from ..levels import TableConverter
import pkgutil

# __all__ = []


def get_level_converter(level):
    if level == 'row':
        return RowConverter
    elif level == 'cell':
        return CellConverter
    elif level == 'column':
        return ColumnConverter
    else:
        return TableConverter


CONVERTERS = {}


for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    # __all__.append(module_name)

    module = loader.find_module(
        module_name).load_module(module_name)

    if not hasattr(module, 'level'):
        continue

    converter = get_level_converter(module.level)

    CONVERTERS[module_name] = converter(
        name=module_name,
        asserter=module.asserter,
        converter=module.converter
    )


# TODO: Column version
# TODO:
# 1. keys are customized functions
# 2. design an easy way to direct how to sort

# TODO, level show in the module file name, not forced to do that, because that will give less choice to name the function
