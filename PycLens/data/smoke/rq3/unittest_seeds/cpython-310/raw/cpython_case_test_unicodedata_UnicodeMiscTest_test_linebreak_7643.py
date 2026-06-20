# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_linebreak_7643

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(65536):
        lines = (chr(i) + 'A').splitlines()
        if i in (10, 11, 12, 13, 133, 28, 29, 30, 8232, 8233):
            self.assertEqual(len(lines), 2, '\\u%.4x should be a linebreak' % i)
        else:
            self.assertEqual(len(lines), 1, '\\u%.4x should not be a linebreak' % i)
