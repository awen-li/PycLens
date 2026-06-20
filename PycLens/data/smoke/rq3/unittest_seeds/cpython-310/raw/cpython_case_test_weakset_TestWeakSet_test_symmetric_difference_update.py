# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_symmetric_difference_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    retval = self.s.symmetric_difference_update(self.items2)
    self.assertEqual(retval, None)
    for c in self.items + self.items2:
        if (c in self.items) ^ (c in self.items2):
            self.assertIn(c, self.s)
        else:
            self.assertNotIn(c, self.s)
    self.assertRaises(TypeError, self.s.symmetric_difference_update, [[]])
