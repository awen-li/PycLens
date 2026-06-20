# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_sigpending

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import os\n            import signal\n\n            def handler(signum, frame):\n                1/0\n\n            signum = signal.SIGUSR1\n            signal.signal(signum, handler)\n\n            signal.pthread_sigmask(signal.SIG_BLOCK, [signum])\n            os.kill(os.getpid(), signum)\n            pending = signal.sigpending()\n            for sig in pending:\n                assert isinstance(sig, signal.Signals), repr(pending)\n            if pending != {signum}:\n                raise Exception(\'%s != {%s}\' % (pending, signum))\n            try:\n                signal.pthread_sigmask(signal.SIG_UNBLOCK, [signum])\n            except ZeroDivisionError:\n                pass\n            else:\n                raise Exception("ZeroDivisionError not raised")\n        '
    assert_python_ok('-c', code)
