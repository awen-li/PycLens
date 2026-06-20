# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_exhausted_reverse_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertEqual(list(a), list(self.example))
    exhit = reversed(a)
    empit = reversed(a)
    for x in exhit:
        next(empit)
    a.insert(0, self.outside)
    self.assertEqual(list(exhit), [])
    self.assertEqual(list(empit), [])
    self.assertEqual(list(a), [self.outside] + list(self.example))
