# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_max_workers_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for number in (0, -1):
        with self.assertRaisesRegex(ValueError, 'max_workers must be greater than 0'):
            self.executor_type(max_workers=number)
