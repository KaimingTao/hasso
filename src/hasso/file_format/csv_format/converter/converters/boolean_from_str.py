BOOLEAN_TABLE = {
    True: ('true', 'yes', '1'),
    False: ('false', 'no', '0'),
}


level = 'column'
asserter = lambda x: type(x) == str
# TODO should test all cell in the column
converter = lambda x: {
            i: k
            for k, v in BOOLEAN_TABLE
            for i in v
        }.get(x, x)
