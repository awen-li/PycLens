# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_category

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.category('\ufffe'), 'Cn')
    self.assertEqual(self.db.category('a'), 'Ll')
    self.assertEqual(self.db.category('A'), 'Lu')
    self.assertEqual(self.db.category('𠀀'), 'Lo')
    self.assertEqual(self.db.category('𐄪'), 'No')
    self.assertRaises(TypeError, self.db.category)
    self.assertRaises(TypeError, self.db.category, 'xx')
