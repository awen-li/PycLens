# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_formatting_huge_precision_c_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import INT_MAX
    format_string = '%.{}f'.format(INT_MAX + 1)
    with self.assertRaises(ValueError):
        result = format_string % 2.34
