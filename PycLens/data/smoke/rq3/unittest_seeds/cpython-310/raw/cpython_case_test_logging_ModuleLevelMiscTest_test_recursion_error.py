# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ModuleLevelMiscTest_test_recursion_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import logging\n\n            def rec():\n                logging.error("foo")\n                rec()\n\n            rec()\n        ')
    (rc, out, err) = assert_python_failure('-c', code)
    err = err.decode()
    self.assertNotIn('Cannot recover from stack overflow.', err)
    self.assertEqual(rc, 1)
