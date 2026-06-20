# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_result_with_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def notification():
        time.sleep(1)
        f1.set_result(42)
    f1 = create_future(state=PENDING)
    t = threading.Thread(target=notification)
    t.start()
    self.assertEqual(f1.result(timeout=5), 42)
    t.join()
