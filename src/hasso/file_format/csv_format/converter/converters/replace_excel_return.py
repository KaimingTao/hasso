level = 'cell'
asserter = lambda x: (x is str) and ('_x000D_' in x)
converter = lambda x: x.replace('_x000D_\n', '\n')
