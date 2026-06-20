# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_exception_with_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def notification():
        time.sleep(1)
        with f1._condition:
            f1._state = FINISHED
            f1._exception = OSError()
            f1._condition.notify_all()
    f1 = create_future(state=PENDING)
    t = threading.Thread(target=notification)
    t.start()
    self.assertTrue(isinstance(f1.exception(timeout=support.SHORT_TIMEOUT), OSError))
    t.join()
