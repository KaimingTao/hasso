def sort_table(table, keys=[]):
    if not keys:
        return

    def sorter(row):
        result = []
        for key in keys:
            result.append(row[key])
        return tuple(result)

    return sorted(table, key=sorter)


level = 'table'
asserter = True
converter = sort_table
