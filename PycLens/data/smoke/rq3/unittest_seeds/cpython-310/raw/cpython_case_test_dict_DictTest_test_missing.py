# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(hasattr(dict, '__missing__'))
    self.assertFalse(hasattr({}, '__missing__'))

    class D(dict):

        def __missing__(self, key):
            return 42
    d = D({1: 2, 3: 4})
    self.assertEqual(d[1], 2)
    self.assertEqual(d[3], 4)
    self.assertNotIn(2, d)
    self.assertNotIn(2, d.keys())
    self.assertEqual(d[2], 42)

    class E(dict):

        def __missing__(self, key):
            raise RuntimeError(key)
    e = E()
    with self.assertRaises(RuntimeError) as c:
        e[42]
    self.assertEqual(c.exception.args, (42,))

    class F(dict):

        def __init__(self):
            self.__missing__ = lambda key: None
    f = F()
    with self.assertRaises(KeyError) as c:
        f[42]
    self.assertEqual(c.exception.args, (42,))

    class G(dict):
        pass
    g = G()
    with self.assertRaises(KeyError) as c:
        g[42]
    self.assertEqual(c.exception.args, (42,))
