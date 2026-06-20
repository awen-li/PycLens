# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_isinstance

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
    self.assertTrue(isinstance(c, C))
    self.assertTrue(isinstance(d, C))
    self.assertTrue(not isinstance(e, C))
    self.assertTrue(not isinstance(c, D))
    self.assertTrue(not isinstance('foo', E))
    self.assertRaises(TypeError, isinstance, E, 'foo')
    self.assertRaises(TypeError, isinstance)
