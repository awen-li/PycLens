# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    y = 2

    def f(x, width):
        return f'x={x * y:{width}}'
    self.assertEqual(f('foo', 10), 'x=foofoo    ')
    x = 'bar'
    self.assertEqual(f(10, 10), 'x=        20')
