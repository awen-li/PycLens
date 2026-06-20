# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: FinalizeTestCase_test_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = self.A()
    res = []
    f1 = weakref.finalize(a, res.append, 'f1')
    f2 = weakref.finalize(a, res.append, 'f2')
    f3 = weakref.finalize(a, res.append, 'f3')
    f4 = weakref.finalize(a, res.append, 'f4')
    f5 = weakref.finalize(a, res.append, 'f5')
    del f1, f4
    self.assertTrue(f2.alive)
    self.assertTrue(f3.alive)
    self.assertTrue(f5.alive)
    self.assertTrue(f5.detach())
    self.assertFalse(f5.alive)
    f5()
    res.append('A')
    f3()
    self.assertFalse(f3.alive)
    res.append('B')
    f3()
    res.append('C')
    del a
    self._collect_if_necessary()
    self.assertFalse(f2.alive)
    res.append('D')
    f2()
    expected = ['A', 'f3', 'B', 'C', 'f4', 'f2', 'f1', 'D']
    self.assertEqual(res, expected)
