# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_exhausted_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertEqual(list(a), list(self.example))
    exhit = iter(a)
    empit = iter(a)
    for x in exhit:
        next(empit)
    a.append(self.outside)
    self.assertEqual(list(exhit), [])
    self.assertEqual(list(empit), [self.outside])
    self.assertEqual(list(a), list(self.example) + [self.outside])
