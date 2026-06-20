# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testformat('€=%f', (1.0,), '€=1.000000')
    self.assertEqual(format('abc', '\u2007<5'), 'abc\u2007\u2007')
    self.assertEqual(format(123, '\u2007<5'), '123\u2007\u2007')
    self.assertEqual(format(12.3, '\u2007<6'), '12.3\u2007\u2007')
    self.assertEqual(format(0j, '\u2007<4'), '0j\u2007\u2007')
    self.assertEqual(format(1 + 2j, '\u2007<8'), '(1+2j)\u2007\u2007')
    self.assertEqual(format('abc', '\u2007>5'), '\u2007\u2007abc')
    self.assertEqual(format(123, '\u2007>5'), '\u2007\u2007123')
    self.assertEqual(format(12.3, '\u2007>6'), '\u2007\u200712.3')
    self.assertEqual(format(1 + 2j, '\u2007>8'), '\u2007\u2007(1+2j)')
    self.assertEqual(format(0j, '\u2007>4'), '\u2007\u20070j')
    self.assertEqual(format('abc', '\u2007^5'), '\u2007abc\u2007')
    self.assertEqual(format(123, '\u2007^5'), '\u2007123\u2007')
    self.assertEqual(format(12.3, '\u2007^6'), '\u200712.3\u2007')
    self.assertEqual(format(1 + 2j, '\u2007^8'), '\u2007(1+2j)\u2007')
    self.assertEqual(format(0j, '\u2007^4'), '\u20070j\u2007')
