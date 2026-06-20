# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_digit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.digit('A', None), None)
    self.assertEqual(self.db.digit('9'), 9)
    self.assertEqual(self.db.digit('⅛', None), None)
    self.assertEqual(self.db.digit('⑨'), 9)
    self.assertEqual(self.db.digit('𠀀', None), None)
    self.assertEqual(self.db.digit('𝟽'), 7)
    self.assertRaises(TypeError, self.db.digit)
    self.assertRaises(TypeError, self.db.digit, 'xx')
    self.assertRaises(ValueError, self.db.digit, 'x')
