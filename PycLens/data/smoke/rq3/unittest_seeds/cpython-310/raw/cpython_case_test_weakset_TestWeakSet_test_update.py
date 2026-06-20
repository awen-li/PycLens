# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    retval = self.s.update(self.items2)
    self.assertEqual(retval, None)
    for c in self.items + self.items2:
        self.assertIn(c, self.s)
    self.assertRaises(TypeError, self.s.update, [[]])
