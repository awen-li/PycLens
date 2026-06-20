# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolWaitTests_test_pending_calls_race

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    event = threading.Event()

    def future_func():
        event.wait()
    oldswitchinterval = sys.getswitchinterval()
    sys.setswitchinterval(1e-06)
    try:
        fs = {self.executor.submit(future_func) for i in range(100)}
        event.set()
        futures.wait(fs, return_when=futures.ALL_COMPLETED)
    finally:
        sys.setswitchinterval(oldswitchinterval)
