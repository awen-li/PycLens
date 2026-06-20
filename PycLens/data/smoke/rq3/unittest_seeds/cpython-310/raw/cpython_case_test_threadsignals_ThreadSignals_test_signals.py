# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threadsignals.py
# case: ThreadSignals_test_signals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with threading_helper.wait_threads_exit():
        signalled_all.acquire()
        self.spawnSignallingThread()
        signalled_all.acquire()
    if signal_blackboard[signal.SIGUSR1]['tripped'] == 0 or signal_blackboard[signal.SIGUSR2]['tripped'] == 0:
        try:
            signal.alarm(1)
            signal.pause()
        finally:
            signal.alarm(0)
    self.assertEqual(signal_blackboard[signal.SIGUSR1]['tripped'], 1)
    self.assertEqual(signal_blackboard[signal.SIGUSR1]['tripped_by'], thread.get_ident())
    self.assertEqual(signal_blackboard[signal.SIGUSR2]['tripped'], 1)
    self.assertEqual(signal_blackboard[signal.SIGUSR2]['tripped_by'], thread.get_ident())
    signalled_all.release()
