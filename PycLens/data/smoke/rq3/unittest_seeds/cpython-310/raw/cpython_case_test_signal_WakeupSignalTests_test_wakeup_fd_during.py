# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupSignalTests_test_wakeup_fd_during

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wakeup('def test():\n            import select\n            import time\n\n            TIMEOUT_FULL = 10\n            TIMEOUT_HALF = 5\n\n            class InterruptSelect(Exception):\n                pass\n\n            def handler(signum, frame):\n                raise InterruptSelect\n            signal.signal(signal.SIGALRM, handler)\n\n            signal.alarm(1)\n            before_time = time.monotonic()\n            # We attempt to get a signal during the select call\n            try:\n                select.select([read], [], [], TIMEOUT_FULL)\n            except InterruptSelect:\n                pass\n            else:\n                raise Exception("select() was not interrupted")\n            after_time = time.monotonic()\n            dt = after_time - before_time\n            if dt >= TIMEOUT_HALF:\n                raise Exception("%s >= %s" % (dt, TIMEOUT_HALF))\n        ', signal.SIGALRM)
