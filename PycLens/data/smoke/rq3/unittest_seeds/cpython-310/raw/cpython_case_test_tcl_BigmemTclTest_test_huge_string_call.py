# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: BigmemTclTest_test_huge_string_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = ' ' * size
    self.assertRaises(OverflowError, self.interp.call, 'string', 'index', value, 0)
