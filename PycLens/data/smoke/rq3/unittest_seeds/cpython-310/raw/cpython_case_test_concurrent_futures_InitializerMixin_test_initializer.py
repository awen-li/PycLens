# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: InitializerMixin_test_initializer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    futures = [self.executor.submit(get_init_status) for _ in range(self.worker_count)]
    for f in futures:
        self.assertEqual(f.result(), 'initialized')
