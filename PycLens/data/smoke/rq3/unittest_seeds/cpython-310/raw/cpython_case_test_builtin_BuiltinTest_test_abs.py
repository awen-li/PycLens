# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_abs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(abs(0), 0)
    self.assertEqual(abs(1234), 1234)
    self.assertEqual(abs(-1234), 1234)
    self.assertTrue(abs(-sys.maxsize - 1) > 0)
    self.assertEqual(abs(0.0), 0.0)
    self.assertEqual(abs(3.14), 3.14)
    self.assertEqual(abs(-3.14), 3.14)
    self.assertRaises(TypeError, abs, 'a')
    self.assertEqual(abs(True), 1)
    self.assertEqual(abs(False), 0)
    self.assertRaises(TypeError, abs)
    self.assertRaises(TypeError, abs, None)

    class AbsClass(object):

        def __abs__(self):
            return -5
    self.assertEqual(abs(AbsClass()), -5)
