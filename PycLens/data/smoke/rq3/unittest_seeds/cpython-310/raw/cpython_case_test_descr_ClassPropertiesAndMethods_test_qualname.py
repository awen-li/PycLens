# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_qualname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    descriptors = [str.lower, complex.real, float.real, int.__add__]
    types = ['method', 'member', 'getset', 'wrapper']
    for (d, n) in zip(descriptors, types):
        self.assertEqual(type(d).__name__, n + '_descriptor')
    for d in descriptors:
        qualname = d.__objclass__.__qualname__ + '.' + d.__name__
        self.assertEqual(d.__qualname__, qualname)
    self.assertEqual(str.lower.__qualname__, 'str.lower')
    self.assertEqual(complex.real.__qualname__, 'complex.real')
    self.assertEqual(float.real.__qualname__, 'float.real')
    self.assertEqual(int.__add__.__qualname__, 'int.__add__')

    class X:
        pass
    with self.assertRaises(TypeError):
        del X.__qualname__
    self.assertRaises(TypeError, type.__dict__['__qualname__'].__set__, str, 'Oink')
    global Y

    class Y:

        class Inside:
            pass
    self.assertEqual(Y.__qualname__, 'Y')
    self.assertEqual(Y.Inside.__qualname__, 'Y.Inside')
