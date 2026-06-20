# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_weakvaluedict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __init__(self, i):
            self.i = i
    (a, b, c, d) = [C(i) for i in range(4)]
    u = weakref.WeakValueDictionary()
    u[a] = b
    u[c] = d
    v = copy.deepcopy(u)
    self.assertNotEqual(v, u)
    self.assertEqual(len(v), 2)
    ((x, y), (z, t)) = sorted(v.items(), key=lambda pair: pair[0].i)
    self.assertIsNot(x, a)
    self.assertEqual(x.i, a.i)
    self.assertIs(y, b)
    self.assertIsNot(z, c)
    self.assertEqual(z.i, c.i)
    self.assertIs(t, d)
    del x, y, z, t
    del d
    support.gc_collect()
    self.assertEqual(len(v), 1)
