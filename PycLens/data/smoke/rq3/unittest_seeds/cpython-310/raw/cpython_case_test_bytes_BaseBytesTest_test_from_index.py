# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test([Indexable(), Indexable(1), Indexable(254), Indexable(255)])
    self.assertEqual(list(b), [0, 1, 254, 255])
    self.assertRaises(ValueError, self.type2test, [Indexable(-1)])
    self.assertRaises(ValueError, self.type2test, [Indexable(256)])
