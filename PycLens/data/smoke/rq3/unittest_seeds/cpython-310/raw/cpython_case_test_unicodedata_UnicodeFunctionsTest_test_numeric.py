# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_numeric

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.numeric('A', None), None)
    self.assertEqual(self.db.numeric('9'), 9)
    self.assertEqual(self.db.numeric('⅛'), 0.125)
    self.assertEqual(self.db.numeric('⑨'), 9.0)
    self.assertEqual(self.db.numeric('꘧'), 7.0)
    self.assertEqual(self.db.numeric('𠀀', None), None)
    self.assertEqual(self.db.numeric('𐄪'), 9000)
    self.assertRaises(TypeError, self.db.numeric)
    self.assertRaises(TypeError, self.db.numeric, 'xx')
    self.assertRaises(ValueError, self.db.numeric, 'x')
