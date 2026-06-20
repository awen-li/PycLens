# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_memory_error_in_PyErr_PrintEx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import _testcapi\n            class C(): pass\n            _testcapi.set_nomemory(0, %d)\n            C()\n        '
    for i in range(1, 20):
        (rc, out, err) = script_helper.assert_python_failure('-c', code % i)
        self.assertIn(rc, (1, 120))
        self.assertIn(b'MemoryError', err)
