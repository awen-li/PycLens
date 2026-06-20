# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_pthread_kill_main_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if True:\n            import threading\n            import signal\n            import sys\n\n            def handler(signum, frame):\n                sys.exit(3)\n\n            signal.signal(signal.SIGUSR1, handler)\n            signal.pthread_kill(threading.get_ident(), signal.SIGUSR1)\n            sys.exit(2)\n        '
    with spawn_python('-c', code) as process:
        (stdout, stderr) = process.communicate()
        exitcode = process.wait()
        if exitcode != 3:
            raise Exception('Child error (exit code %s): %s' % (exitcode, stdout))
