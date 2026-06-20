# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: SubinterpThreadingTests_test_daemon_threads_fatal_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    subinterp_code = f'if 1:\n            import os\n            import threading\n            import time\n\n            def f():\n                # Make sure the daemon thread is still running when\n                # Py_EndInterpreter is called.\n                time.sleep({test.support.SHORT_TIMEOUT})\n            threading.Thread(target=f, daemon=True).start()\n            '
    script = 'if 1:\n            import _testcapi\n\n            _testcapi.run_in_subinterp(%r)\n            ' % (subinterp_code,)
    with test.support.SuppressCrashReport():
        (rc, out, err) = assert_python_failure('-c', script)
    self.assertIn('Fatal Python error: Py_EndInterpreter: not the last thread', err.decode())
