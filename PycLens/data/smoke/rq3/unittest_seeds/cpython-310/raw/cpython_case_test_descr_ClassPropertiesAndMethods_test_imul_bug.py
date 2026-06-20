# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_imul_bug

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __imul__(self, other):
            return (self, other)
    x = C()
    y = x
    y *= 1.0
    self.assertEqual(y, (x, 1.0))
    y = x
    y *= 2
    self.assertEqual(y, (x, 2))
    y = x
    y *= 3
    self.assertEqual(y, (x, 3))
    y = x
    y *= 1 << 100
    self.assertEqual(y, (x, 1 << 100))
    y = x
    y *= None
    self.assertEqual(y, (x, None))
    y = x
    y *= 'foo'
    self.assertEqual(y, (x, 'foo'))
