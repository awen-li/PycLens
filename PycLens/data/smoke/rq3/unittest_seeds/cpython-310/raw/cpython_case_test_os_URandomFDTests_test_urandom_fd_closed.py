# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: URandomFDTests_test_urandom_fd_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import os\n            import sys\n            import test.support\n            os.urandom(4)\n            with test.support.SuppressCrashReport():\n                os.closerange(3, 256)\n            sys.stdout.buffer.write(os.urandom(4))\n            '
    (rc, out, err) = assert_python_ok('-Sc', code)
