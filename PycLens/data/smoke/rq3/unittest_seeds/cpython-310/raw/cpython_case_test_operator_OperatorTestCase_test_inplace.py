# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_inplace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module

    class C(object):

        def __iadd__(self, other):
            return 'iadd'

        def __iand__(self, other):
            return 'iand'

        def __ifloordiv__(self, other):
            return 'ifloordiv'

        def __ilshift__(self, other):
            return 'ilshift'

        def __imod__(self, other):
            return 'imod'

        def __imul__(self, other):
            return 'imul'

        def __imatmul__(self, other):
            return 'imatmul'

        def __ior__(self, other):
            return 'ior'

        def __ipow__(self, other):
            return 'ipow'

        def __irshift__(self, other):
            return 'irshift'

        def __isub__(self, other):
            return 'isub'

        def __itruediv__(self, other):
            return 'itruediv'

        def __ixor__(self, other):
            return 'ixor'

        def __getitem__(self, other):
            return 5
    c = C()
    self.assertEqual(operator.iadd(c, 5), 'iadd')
    self.assertEqual(operator.iand(c, 5), 'iand')
    self.assertEqual(operator.ifloordiv(c, 5), 'ifloordiv')
    self.assertEqual(operator.ilshift(c, 5), 'ilshift')
    self.assertEqual(operator.imod(c, 5), 'imod')
    self.assertEqual(operator.imul(c, 5), 'imul')
    self.assertEqual(operator.imatmul(c, 5), 'imatmul')
    self.assertEqual(operator.ior(c, 5), 'ior')
    self.assertEqual(operator.ipow(c, 5), 'ipow')
    self.assertEqual(operator.irshift(c, 5), 'irshift')
    self.assertEqual(operator.isub(c, 5), 'isub')
    self.assertEqual(operator.itruediv(c, 5), 'itruediv')
    self.assertEqual(operator.ixor(c, 5), 'ixor')
    self.assertEqual(operator.iconcat(c, c), 'iadd')
