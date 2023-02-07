def get_table_header(table):
    headers = []
    for rec in table:
        for key in rec.keys():
            if key not in headers:
                headers.append(key)

    return headers
