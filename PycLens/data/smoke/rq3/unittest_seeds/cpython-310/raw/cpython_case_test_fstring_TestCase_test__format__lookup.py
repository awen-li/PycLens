# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test__format__lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __format__(self, spec):
            return 'class'
    x = X()
    y = X()
    y.__format__ = types.MethodType(lambda self, spec: 'instance', y)
    self.assertEqual(f'{y}', format(y))
    self.assertEqual(f'{y}', 'class')
    self.assertEqual(format(x), format(y))
    self.assertEqual(x.__format__(''), 'class')
    self.assertEqual(y.__format__(''), 'instance')
    self.assertEqual(type(x).__format__(x, ''), 'class')
    self.assertEqual(type(y).__format__(y, ''), 'class')
