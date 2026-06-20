# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_issue16335

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b'\\N{SPACE' + b'x' * (UINT_MAX + 1) + b'}'
    self.assertEqual(len(x), len(b'\\N{SPACE}') + (UINT_MAX + 1))
    self.assertRaisesRegex(UnicodeError, 'unknown Unicode character name', x.decode, 'unicode-escape')
