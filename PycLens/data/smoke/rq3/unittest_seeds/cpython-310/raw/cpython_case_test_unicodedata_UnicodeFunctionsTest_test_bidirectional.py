# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_bidirectional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.bidirectional('\ufffe'), '')
    self.assertEqual(self.db.bidirectional(' '), 'WS')
    self.assertEqual(self.db.bidirectional('A'), 'L')
    self.assertEqual(self.db.bidirectional('𠀀'), 'L')
    self.assertRaises(TypeError, self.db.bidirectional)
    self.assertRaises(TypeError, self.db.bidirectional, 'xx')
