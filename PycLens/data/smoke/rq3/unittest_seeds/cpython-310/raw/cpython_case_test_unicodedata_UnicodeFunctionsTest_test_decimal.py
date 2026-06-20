# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_decimal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.decimal('A', None), None)
    self.assertEqual(self.db.decimal('9'), 9)
    self.assertEqual(self.db.decimal('⅛', None), None)
    self.assertEqual(self.db.decimal('⑨', None), None)
    self.assertEqual(self.db.decimal('𠀀', None), None)
    self.assertEqual(self.db.decimal('𝟽'), 7)
    self.assertRaises(TypeError, self.db.decimal)
    self.assertRaises(TypeError, self.db.decimal, 'xx')
    self.assertRaises(ValueError, self.db.decimal, 'x')
