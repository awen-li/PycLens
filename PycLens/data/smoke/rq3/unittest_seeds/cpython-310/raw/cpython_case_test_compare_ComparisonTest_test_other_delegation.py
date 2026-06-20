# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_other_delegation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ops = (('__eq__', lambda a, b: a == b), ('__lt__', lambda a, b: a < b), ('__le__', lambda a, b: a <= b), ('__gt__', lambda a, b: a > b), ('__ge__', lambda a, b: a >= b))
    for (name, func) in ops:
        with self.subTest(name):

            def unexpected(*args):
                self.fail('Unexpected operator method called')

            class C:
                __ne__ = unexpected
            for (other, _) in ops:
                if other != name:
                    setattr(C, other, unexpected)
            if name == '__eq__':
                self.assertIs(func(C(), object()), False)
            else:
                self.assertRaises(TypeError, func, C(), object())
