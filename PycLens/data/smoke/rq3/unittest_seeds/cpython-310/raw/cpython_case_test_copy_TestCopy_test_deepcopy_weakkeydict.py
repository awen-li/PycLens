# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_weakkeydict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __init__(self, i):
            self.i = i
    (a, b, c, d) = [C(i) for i in range(4)]
    u = weakref.WeakKeyDictionary()
    u[a] = b
    u[c] = d
    v = copy.deepcopy(u)
    self.assertNotEqual(v, u)
    self.assertEqual(len(v), 2)
    self.assertIsNot(v[a], b)
    self.assertIsNot(v[c], d)
    self.assertEqual(v[a].i, b.i)
    self.assertEqual(v[c].i, d.i)
    del c
    support.gc_collect()
    self.assertEqual(len(v), 1)
