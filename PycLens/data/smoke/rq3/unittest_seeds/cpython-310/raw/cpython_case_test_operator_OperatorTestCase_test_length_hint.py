# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_length_hint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module

    class X(object):

        def __init__(self, value):
            self.value = value

        def __length_hint__(self):
            if type(self.value) is type:
                raise self.value
            else:
                return self.value
    self.assertEqual(operator.length_hint([], 2), 0)
    self.assertEqual(operator.length_hint(iter([1, 2, 3])), 3)
    self.assertEqual(operator.length_hint(X(2)), 2)
    self.assertEqual(operator.length_hint(X(NotImplemented), 4), 4)
    self.assertEqual(operator.length_hint(X(TypeError), 12), 12)
    with self.assertRaises(TypeError):
        operator.length_hint(X('abc'))
    with self.assertRaises(ValueError):
        operator.length_hint(X(-2))
    with self.assertRaises(LookupError):
        operator.length_hint(X(LookupError))
