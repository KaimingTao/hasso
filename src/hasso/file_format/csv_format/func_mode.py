def get_func_mode(func):

    func_name = func.__name__

    if '_' not in func_name:
        func_mode = None
    else:
        func_mode = func_name.split('_')[0]

    assert func_mode in ('load', 'dump'), f'{func_mode} not accepted'

    return func_mode
