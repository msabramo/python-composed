def compose(*funcs):
    def f(*args):
        vals = args

        for func in reversed(funcs):
            try:
                vals = func(*vals)
            except TypeError:
                vals = func(*(vals,))

        return vals

    return f
