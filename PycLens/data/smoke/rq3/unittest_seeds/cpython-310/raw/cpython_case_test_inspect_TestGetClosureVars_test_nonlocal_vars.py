# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_nonlocal_vars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _nonlocal_vars(f):
        return inspect.getclosurevars(f).nonlocals

    def make_adder(x):

        def add(y):
            return x + y
        return add

    def curry(func, arg1):
        return lambda arg2: func(arg1, arg2)

    def less_than(a, b):
        return a < b

    def Y(le):

        def g(f):
            return le(lambda x: f(f)(x))
        Y.g_ref = g
        return g(g)

    def check_y_combinator(func):
        self.assertEqual(_nonlocal_vars(func), {'f': Y.g_ref})
    inc = make_adder(1)
    add_two = make_adder(2)
    greater_than_five = curry(less_than, 5)
    self.assertEqual(_nonlocal_vars(inc), {'x': 1})
    self.assertEqual(_nonlocal_vars(add_two), {'x': 2})
    self.assertEqual(_nonlocal_vars(greater_than_five), {'arg1': 5, 'func': less_than})
    self.assertEqual(_nonlocal_vars((lambda x: lambda y: x + y)(3)), {'x': 3})
    Y(check_y_combinator)
