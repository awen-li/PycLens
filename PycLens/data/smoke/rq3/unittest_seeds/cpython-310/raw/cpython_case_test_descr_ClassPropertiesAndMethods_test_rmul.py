# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_rmul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __mul__(self, other):
            return 'mul'

        def __rmul__(self, other):
            return 'rmul'
    a = C()
    self.assertEqual(a * 2, 'mul')
    self.assertEqual(a * 2.2, 'mul')
    self.assertEqual(2 * a, 'rmul')
    self.assertEqual(2.2 * a, 'rmul')
