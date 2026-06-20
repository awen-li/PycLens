# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(''), "''")
    self.assertEqual(repr(0), '0')
    self.assertEqual(repr(()), '()')
    self.assertEqual(repr([]), '[]')
    self.assertEqual(repr({}), '{}')
    a = []
    a.append(a)
    self.assertEqual(repr(a), '[[...]]')
    a = {}
    a[0] = a
    self.assertEqual(repr(a), '{0: {...}}')
