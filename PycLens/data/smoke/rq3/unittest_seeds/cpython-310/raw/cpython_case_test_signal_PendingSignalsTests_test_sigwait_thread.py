# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_sigwait_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert_python_ok('-c', 'if True:\n            import os, threading, sys, time, signal\n\n            # the default handler terminates the process\n            signum = signal.SIGUSR1\n\n            def kill_later():\n                # wait until the main thread is waiting in sigwait()\n                time.sleep(1)\n                os.kill(os.getpid(), signum)\n\n            # the signal must be blocked by all the threads\n            signal.pthread_sigmask(signal.SIG_BLOCK, [signum])\n            killer = threading.Thread(target=kill_later)\n            killer.start()\n            received = signal.sigwait([signum])\n            if received != signum:\n                print("sigwait() received %s, not %s" % (received, signum),\n                      file=sys.stderr)\n                sys.exit(1)\n            killer.join()\n            # unblock the signal, which should have been cleared by sigwait()\n            signal.pthread_sigmask(signal.SIG_UNBLOCK, [signum])\n        ')
