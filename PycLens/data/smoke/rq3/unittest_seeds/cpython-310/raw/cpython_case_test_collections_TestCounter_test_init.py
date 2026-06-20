# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(Counter(self=42).items()), [('self', 42)])
    self.assertEqual(list(Counter(iterable=42).items()), [('iterable', 42)])
    self.assertEqual(list(Counter(iterable=None).items()), [('iterable', None)])
    self.assertRaises(TypeError, Counter, 42)
    self.assertRaises(TypeError, Counter, (), ())
    self.assertRaises(TypeError, Counter.__init__)
