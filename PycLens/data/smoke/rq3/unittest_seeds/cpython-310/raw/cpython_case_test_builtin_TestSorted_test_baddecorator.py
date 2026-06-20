# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestSorted_test_baddecorator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'The quick Brown fox Jumped over The lazy Dog'.split()
    self.assertRaises(TypeError, sorted, data, None, lambda x, y: 0)
