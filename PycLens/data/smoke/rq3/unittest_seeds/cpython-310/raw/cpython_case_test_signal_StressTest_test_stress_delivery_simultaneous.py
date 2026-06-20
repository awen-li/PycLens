# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: StressTest_test_stress_delivery_simultaneous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = self.decide_itimer_count()
    sigs = []

    def handler(signum, frame):
        sigs.append(signum)
    self.setsig(signal.SIGUSR1, handler)
    self.setsig(signal.SIGALRM, handler)
    expected_sigs = 0
    deadline = time.monotonic() + support.SHORT_TIMEOUT
    while expected_sigs < N:
        signal.setitimer(signal.ITIMER_REAL, 1e-06 + random.random() * 1e-05)
        os.kill(os.getpid(), signal.SIGUSR1)
        expected_sigs += 2
        while len(sigs) < expected_sigs and time.monotonic() < deadline:
            time.sleep(1e-05)
    self.assertEqual(len(sigs), N, 'Some signals were lost')
