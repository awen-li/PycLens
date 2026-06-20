# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupSignalTests_test_wakeup_write_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n        import _testcapi\n        import errno\n        import os\n        import signal\n        import sys\n        from test.support import captured_stderr\n\n        def handler(signum, frame):\n            1/0\n\n        signal.signal(signal.SIGALRM, handler)\n        r, w = os.pipe()\n        os.set_blocking(r, False)\n\n        # Set wakeup_fd a read-only file descriptor to trigger the error\n        signal.set_wakeup_fd(r)\n        try:\n            with captured_stderr() as err:\n                signal.raise_signal(signal.SIGALRM)\n        except ZeroDivisionError:\n            # An ignored exception should have been printed out on stderr\n            err = err.getvalue()\n            if (\'Exception ignored when trying to write to the signal wakeup fd\'\n                not in err):\n                raise AssertionError(err)\n            if (\'OSError: [Errno %d]\' % errno.EBADF) not in err:\n                raise AssertionError(err)\n        else:\n            raise AssertionError("ZeroDivisionError not raised")\n\n        os.close(r)\n        os.close(w)\n        '
    (r, w) = os.pipe()
    try:
        os.write(r, b'x')
    except OSError:
        pass
    else:
        self.skipTest("OS doesn't report write() error on the read end of a pipe")
    finally:
        os.close(r)
        os.close(w)
    assert_python_ok('-c', code)
