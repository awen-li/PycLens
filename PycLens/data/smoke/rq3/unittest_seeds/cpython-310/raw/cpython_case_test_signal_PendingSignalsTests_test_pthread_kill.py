# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_pthread_kill

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import signal\n            import threading\n            import sys\n\n            signum = signal.SIGUSR1\n\n            def handler(signum, frame):\n                1/0\n\n            signal.signal(signum, handler)\n\n            tid = threading.get_ident()\n            try:\n                signal.pthread_kill(tid, signum)\n            except ZeroDivisionError:\n                pass\n            else:\n                raise Exception("ZeroDivisionError not raised")\n        '
    assert_python_ok('-c', code)
