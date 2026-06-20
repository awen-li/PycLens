# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: AtexitTests_test_atexit_after_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            import threading\n\n            def func():\n                pass\n\n            def run_last():\n                threading._register_atexit(func)\n\n            threading._register_atexit(run_last)\n        ')
    self.assertTrue(err)
    self.assertIn("RuntimeError: can't register atexit after shutdown", err.decode())
