# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolExecutorTest_test_map_submits_without_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    finished = []

    def record_finished(n):
        finished.append(n)
    self.executor.map(record_finished, range(10))
    self.executor.shutdown(wait=True)
    self.assertCountEqual(finished, range(10))
