# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_truth_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if None:
        self.fail('None is true instead of false')
    if 0:
        self.fail('0 is true instead of false')
    if 0.0:
        self.fail('0.0 is true instead of false')
    if '':
        self.fail("'' is true instead of false")
    if not 1:
        self.fail('1 is false instead of true')
    if not 1.0:
        self.fail('1.0 is false instead of true')
    if not 'x':
        self.fail("'x' is false instead of true")
    if not {'x': 1}:
        self.fail("{'x': 1} is false instead of true")

    def f():
        pass

    class C:
        pass
    x = C()
    if not f:
        self.fail('f is false instead of true')
    if not C:
        self.fail('C is false instead of true')
    if not sys:
        self.fail('sys is false instead of true')
    if not x:
        self.fail('x is false instead of true')
