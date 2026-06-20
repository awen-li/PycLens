# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_map_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    results = []
    try:
        for i in self.executor.map(time.sleep, [0, 0, 6], timeout=5):
            results.append(i)
    except futures.TimeoutError:
        pass
    else:
        self.fail('expected TimeoutError')
    self.assertEqual([None, None], results)
