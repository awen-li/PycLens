# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: FinalizeTestCase_test_finalize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def add(x, y, z):
        res.append(x + y + z)
        return x + y + z
    a = self.A()
    res = []
    f = weakref.finalize(a, add, 67, 43, z=89)
    self.assertEqual(f.alive, True)
    self.assertEqual(f.peek(), (a, add, (67, 43), {'z': 89}))
    self.assertEqual(f(), 199)
    self.assertEqual(f(), None)
    self.assertEqual(f(), None)
    self.assertEqual(f.peek(), None)
    self.assertEqual(f.detach(), None)
    self.assertEqual(f.alive, False)
    self.assertEqual(res, [199])
    res = []
    f = weakref.finalize(a, add, 67, 43, 89)
    self.assertEqual(f.peek(), (a, add, (67, 43, 89), {}))
    self.assertEqual(f.detach(), (a, add, (67, 43, 89), {}))
    self.assertEqual(f(), None)
    self.assertEqual(f(), None)
    self.assertEqual(f.peek(), None)
    self.assertEqual(f.detach(), None)
    self.assertEqual(f.alive, False)
    self.assertEqual(res, [])
    res = []
    f = weakref.finalize(a, add, x=67, y=43, z=89)
    del a
    self._collect_if_necessary()
    self.assertEqual(f(), None)
    self.assertEqual(f(), None)
    self.assertEqual(f.peek(), None)
    self.assertEqual(f.detach(), None)
    self.assertEqual(f.alive, False)
    self.assertEqual(res, [199])
