# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_recursion_normalizing_with_no_memory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import _testcapi\n            class C(): pass\n            def recurse(cnt):\n                cnt -= 1\n                if cnt:\n                    recurse(cnt)\n                else:\n                    _testcapi.set_nomemory(0)\n                    C()\n            recurse(16)\n        '
    with SuppressCrashReport():
        (rc, out, err) = script_helper.assert_python_failure('-c', code)
        self.assertIn(b'Fatal Python error: _PyErr_NormalizeException: Cannot recover from MemoryErrors while normalizing exceptions.', err)
