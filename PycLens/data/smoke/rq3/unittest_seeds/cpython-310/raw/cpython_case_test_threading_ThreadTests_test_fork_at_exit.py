# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_fork_at_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import atexit\n            import os\n            import sys\n            from test.support import wait_process\n\n            # Import the threading module to register its "at fork" callback\n            import threading\n\n            def exit_handler():\n                pid = os.fork()\n                if not pid:\n                    print("child process ok", file=sys.stderr, flush=True)\n                    # child process\n                else:\n                    wait_process(pid, exitcode=0)\n\n            # exit_handler() will be called after threading._shutdown()\n            atexit.register(exit_handler)\n        ')
    (_, out, err) = assert_python_ok('-c', code)
    self.assertEqual(out, b'')
    self.assertEqual(err.rstrip(), b'child process ok')
