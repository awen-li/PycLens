# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_issubclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass

    class D(C):
        pass

    class E:
        pass
    c = C()
    d = D()
    e = E()
    self.assertTrue(issubclass(D, C))
    self.assertTrue(issubclass(C, C))
    self.assertTrue(not issubclass(C, D))
    self.assertRaises(TypeError, issubclass, 'foo', E)
    self.assertRaises(TypeError, issubclass, E, 'foo')
    self.assertRaises(TypeError, issubclass)
