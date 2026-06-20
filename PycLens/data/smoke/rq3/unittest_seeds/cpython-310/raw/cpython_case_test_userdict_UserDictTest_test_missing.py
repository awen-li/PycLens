# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userdict.py
# case: UserDictTest_test_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(hasattr(collections.UserDict, '__missing__'), False)

    class D(collections.UserDict):

        def __missing__(self, key):
            return 42
    d = D({1: 2, 3: 4})
    self.assertEqual(d[1], 2)
    self.assertEqual(d[3], 4)
    self.assertNotIn(2, d)
    self.assertNotIn(2, d.keys())
    self.assertEqual(d[2], 42)

    class E(collections.UserDict):

        def __missing__(self, key):
            raise RuntimeError(key)
    e = E()
    try:
        e[42]
    except RuntimeError as err:
        self.assertEqual(err.args, (42,))
    else:
        self.fail("e[42] didn't raise RuntimeError")

    class F(collections.UserDict):

        def __init__(self):
            self.__missing__ = lambda key: None
            collections.UserDict.__init__(self)
    f = F()
    try:
        f[42]
    except KeyError as err:
        self.assertEqual(err.args, (42,))
    else:
        self.fail("f[42] didn't raise KeyError")

    class G(collections.UserDict):
        pass
    g = G()
    try:
        g[42]
    except KeyError as err:
        self.assertEqual(err.args, (42,))
    else:
        self.fail("g[42] didn't raise KeyError")
