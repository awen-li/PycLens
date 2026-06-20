# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: StressTest_test_stress_modifying_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    signum = signal.SIGUSR1
    num_sent_signals = 0
    num_received_signals = 0
    do_stop = False

    def custom_handler(signum, frame):
        nonlocal num_received_signals
        num_received_signals += 1

    def set_interrupts():
        nonlocal num_sent_signals
        while not do_stop:
            signal.raise_signal(signum)
            num_sent_signals += 1

    def cycle_handlers():
        while num_sent_signals < 100:
            for i in range(20000):
                for handler in [custom_handler, signal.SIG_IGN]:
                    signal.signal(signum, handler)
    old_handler = signal.signal(signum, custom_handler)
    self.addCleanup(signal.signal, signum, old_handler)
    t = threading.Thread(target=set_interrupts)
    try:
        ignored = False
        with support.catch_unraisable_exception() as cm:
            t.start()
            cycle_handlers()
            do_stop = True
            t.join()
            if cm.unraisable is not None:
                self.assertIsInstance(cm.unraisable.exc_value, OSError)
                self.assertIn(f'Signal {signum:d} ignored due to race condition', str(cm.unraisable.exc_value))
                ignored = True
        if not ignored:
            self.assertGreater(num_received_signals, 0)
        self.assertLess(num_received_signals, num_sent_signals)
    finally:
        do_stop = True
        t.join()
