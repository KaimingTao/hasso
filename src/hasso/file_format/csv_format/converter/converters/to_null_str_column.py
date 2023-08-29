NULL_MAP = {
    'NULL': '',
    'NA': '',
    'ND': '',
    'N/A': '',
}

level = 'column'
asserter = lambda x: type(x) == str,
converter = lambda x: NULL_MAP.get(x, x)
