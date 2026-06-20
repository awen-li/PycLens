# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_any

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(any([None, None, None]), False)
    self.assertEqual(any([None, 4, None]), True)
    self.assertRaises(RuntimeError, any, [None, TestFailingBool(), 6])
    self.assertRaises(RuntimeError, any, TestFailingIter())
    self.assertRaises(TypeError, any, 10)
    self.assertRaises(TypeError, any)
    self.assertRaises(TypeError, any, [2, 4, 6], [])
    self.assertEqual(any([]), False)
    self.assertEqual(any([1, TestFailingBool()]), True)
    S = [40, 60, 30]
    self.assertEqual(any((x > 42 for x in S)), True)
    S = [10, 20, 30]
    self.assertEqual(any((x > 42 for x in S)), False)
