# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_python_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(dict, dict))
    self.assertIsInstance({}, dict)
    d = dict()
    self.assertEqual(d, {})
    self.assertIs(d.__class__, dict)
    self.assertIsInstance(d, dict)

    class C(dict):
        state = -1

        def __init__(self_local, *a, **kw):
            if a:
                self.assertEqual(len(a), 1)
                self_local.state = a[0]
            if kw:
                for (k, v) in list(kw.items()):
                    self_local[v] = k

        def __getitem__(self, key):
            return self.get(key, 0)

        def __setitem__(self_local, key, value):
            self.assertIsInstance(key, type(0))
            dict.__setitem__(self_local, key, value)

        def setstate(self, state):
            self.state = state

        def getstate(self):
            return self.state
    self.assertTrue(issubclass(C, dict))
    a1 = C(12)
    self.assertEqual(a1.state, 12)
    a2 = C(foo=1, bar=2)
    self.assertEqual(a2[1] == 'foo' and a2[2], 'bar')
    a = C()
    self.assertEqual(a.state, -1)
    self.assertEqual(a.getstate(), -1)
    a.setstate(0)
    self.assertEqual(a.state, 0)
    self.assertEqual(a.getstate(), 0)
    a.setstate(10)
    self.assertEqual(a.state, 10)
    self.assertEqual(a.getstate(), 10)
    self.assertEqual(a[42], 0)
    a[42] = 24
    self.assertEqual(a[42], 24)
    N = 50
    for i in range(N):
        a[i] = C()
        for j in range(N):
            a[i][j] = i * j
    for i in range(N):
        for j in range(N):
            self.assertEqual(a[i][j], i * j)
