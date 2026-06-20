# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_unbound_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = list[int]
    a = t()
    t.append(a, 'foo')
    self.assertEqual(a, ['foo'])
    x = t.__getitem__(a, 0)
    self.assertEqual(x, 'foo')
    self.assertEqual(t.__len__(a), 1)
