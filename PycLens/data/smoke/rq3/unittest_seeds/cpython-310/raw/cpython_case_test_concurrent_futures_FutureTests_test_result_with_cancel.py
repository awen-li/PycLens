# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_result_with_cancel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def notification():
        time.sleep(1)
        f1.cancel()
    f1 = create_future(state=PENDING)
    t = threading.Thread(target=notification)
    t.start()
    self.assertRaises(futures.CancelledError, f1.result, timeout=support.SHORT_TIMEOUT)
    t.join()
