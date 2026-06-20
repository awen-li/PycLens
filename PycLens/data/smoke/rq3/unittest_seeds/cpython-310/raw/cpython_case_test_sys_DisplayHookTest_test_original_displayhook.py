# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: DisplayHookTest_test_original_displayhook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dh = sys.__displayhook__
    with support.captured_stdout() as out:
        dh(42)
    self.assertEqual(out.getvalue(), '42\n')
    self.assertEqual(builtins._, 42)
    del builtins._
    with support.captured_stdout() as out:
        dh(None)
    self.assertEqual(out.getvalue(), '')
    self.assertTrue(not hasattr(builtins, '_'))
    self.assertRaises(TypeError, dh)
    stdout = sys.stdout
    try:
        del sys.stdout
        self.assertRaises(RuntimeError, dh, 42)
    finally:
        sys.stdout = stdout
