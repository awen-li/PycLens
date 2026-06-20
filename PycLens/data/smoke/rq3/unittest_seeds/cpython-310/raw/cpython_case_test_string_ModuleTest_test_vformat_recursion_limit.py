# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_vformat_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()
    args = ()
    kwargs = dict(i=100)
    with self.assertRaises(ValueError) as err:
        fmt._vformat('{i}', args, kwargs, set(), -1)
    self.assertIn('recursion', str(err.exception))
