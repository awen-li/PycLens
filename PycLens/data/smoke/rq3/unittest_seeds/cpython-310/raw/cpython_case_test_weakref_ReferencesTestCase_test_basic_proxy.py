# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_basic_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    self.check_proxy(o, weakref.proxy(o))
    L = collections.UserList()
    p = weakref.proxy(L)
    self.assertFalse(p, 'proxy for empty UserList should be false')
    p.append(12)
    self.assertEqual(len(L), 1)
    self.assertTrue(p, 'proxy for non-empty UserList should be true')
    p[:] = [2, 3]
    self.assertEqual(len(L), 2)
    self.assertEqual(len(p), 2)
    self.assertIn(3, p, "proxy didn't support __contains__() properly")
    p[1] = 5
    self.assertEqual(L[1], 5)
    self.assertEqual(p[1], 5)
    L2 = collections.UserList(L)
    p2 = weakref.proxy(L2)
    self.assertEqual(p, p2)
    L3 = collections.UserList(range(10))
    p3 = weakref.proxy(L3)
    self.assertEqual(L3[:], p3[:])
    self.assertEqual(L3[5:], p3[5:])
    self.assertEqual(L3[:5], p3[:5])
    self.assertEqual(L3[2:5], p3[2:5])
