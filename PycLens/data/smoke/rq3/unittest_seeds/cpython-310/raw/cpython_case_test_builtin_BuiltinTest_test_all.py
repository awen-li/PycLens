# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(all([2, 4, 6]), True)
    self.assertEqual(all([2, None, 6]), False)
    self.assertRaises(RuntimeError, all, [2, TestFailingBool(), 6])
    self.assertRaises(RuntimeError, all, TestFailingIter())
    self.assertRaises(TypeError, all, 10)
    self.assertRaises(TypeError, all)
    self.assertRaises(TypeError, all, [2, 4, 6], [])
    self.assertEqual(all([]), True)
    self.assertEqual(all([0, TestFailingBool()]), False)
    S = [50, 60]
    self.assertEqual(all((x > 42 for x in S)), True)
    S = [50, 40, 60]
    self.assertEqual(all((x > 42 for x in S)), False)
