# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_combining

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.combining('\ufffe'), 0)
    self.assertEqual(self.db.combining('a'), 0)
    self.assertEqual(self.db.combining('⃡'), 230)
    self.assertEqual(self.db.combining('𠀀'), 0)
    self.assertRaises(TypeError, self.db.combining)
    self.assertRaises(TypeError, self.db.combining, 'xx')
