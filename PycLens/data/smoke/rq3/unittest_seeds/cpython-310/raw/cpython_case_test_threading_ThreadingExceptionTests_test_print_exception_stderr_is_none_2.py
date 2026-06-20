# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadingExceptionTests_test_print_exception_stderr_is_none_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = 'if True:\n            import sys\n            import threading\n            import time\n\n            running = False\n            def run():\n                global running\n                running = True\n                while running:\n                    time.sleep(0.01)\n                1/0\n            sys.stderr = None\n            t = threading.Thread(target=run)\n            t.start()\n            while not running:\n                time.sleep(0.01)\n            running = False\n            t.join()\n            '
    (rc, out, err) = assert_python_ok('-c', script)
    self.assertEqual(out, b'')
    self.assertNotIn('Unhandled exception', err.decode())
