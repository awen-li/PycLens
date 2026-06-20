# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_precision_c_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import INT_MAX
    f = 1.2
    with self.assertRaises(ValueError) as cm:
        format(f, '.%sf' % (INT_MAX + 1))
    c = complex(f)
    with self.assertRaises(ValueError) as cm:
        format(c, '.%sf' % (INT_MAX + 1))
