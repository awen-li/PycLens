# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_hasattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(sys, 'stdout'))
    self.assertRaises(TypeError, hasattr, sys, 1)
    self.assertRaises(TypeError, hasattr)
    self.assertEqual(False, hasattr(sys, chr(sys.maxunicode)))

    class A:

        def __getattr__(self, what):
            raise SystemExit
    self.assertRaises(SystemExit, hasattr, A(), 'b')

    class B:

        def __getattr__(self, what):
            raise ValueError
    self.assertRaises(ValueError, hasattr, B(), 'b')
