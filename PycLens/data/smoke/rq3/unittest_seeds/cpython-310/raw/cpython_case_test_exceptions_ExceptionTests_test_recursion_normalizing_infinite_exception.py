# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_recursion_normalizing_infinite_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "if 1:\n            import _testcapi\n            try:\n                raise _testcapi.RecursingInfinitelyError\n            finally:\n                print('Done.')\n        "
    (rc, out, err) = script_helper.assert_python_failure('-c', code)
    self.assertEqual(rc, 1)
    self.assertIn(b'RecursionError: maximum recursion depth exceeded while normalizing an exception', err)
    self.assertIn(b'Done.', out)
