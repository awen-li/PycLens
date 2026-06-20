# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_mirrored

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.mirrored('\ufffe'), 0)
    self.assertEqual(self.db.mirrored('a'), 0)
    self.assertEqual(self.db.mirrored('∁'), 1)
    self.assertEqual(self.db.mirrored('𠀀'), 0)
    self.assertRaises(TypeError, self.db.mirrored)
    self.assertRaises(TypeError, self.db.mirrored, 'xx')
