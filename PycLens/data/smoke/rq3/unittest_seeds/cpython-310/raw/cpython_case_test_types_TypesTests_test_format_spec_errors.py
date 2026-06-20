# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_format_spec_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, format, 0, '1' * 10000 + 'd')
    self.assertRaises(ValueError, format, 0, '.' + '1' * 10000 + 'd')
    self.assertRaises(ValueError, format, 0, '1' * 1000 + '.' + '1' * 10000 + 'd')
    for code in 'xXobns':
        self.assertRaises(ValueError, format, 0, ',' + code)
