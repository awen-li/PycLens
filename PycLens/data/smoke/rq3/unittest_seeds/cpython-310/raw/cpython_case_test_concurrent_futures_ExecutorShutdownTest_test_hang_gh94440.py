# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorShutdownTest_test_hang_gh94440

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not hasattr(signal, 'alarm'):
        raise unittest.SkipTest('Tested platform does not support the alarm signal')

    def timeout(_signum, _frame):
        raise RuntimeError('timed out waiting for shutdown')
    kwargs = {}
    if getattr(self, 'ctx', None):
        kwargs['mp_context'] = self.get_context()
    executor = self.executor_type(max_workers=1, **kwargs)
    executor.submit(int).result()
    old_handler = signal.signal(signal.SIGALRM, timeout)
    try:
        signal.alarm(5)
        executor.submit(int).cancel()
        executor.shutdown(wait=True)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)
