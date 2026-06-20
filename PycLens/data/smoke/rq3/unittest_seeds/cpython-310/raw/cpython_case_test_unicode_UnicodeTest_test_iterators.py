# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_iterators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = 'ᄑ∢㌳'.__iter__()
    self.assertEqual(next(it), 'ᄑ')
    self.assertEqual(next(it), '∢')
    self.assertEqual(next(it), '㌳')
    self.assertRaises(StopIteration, next, it)
