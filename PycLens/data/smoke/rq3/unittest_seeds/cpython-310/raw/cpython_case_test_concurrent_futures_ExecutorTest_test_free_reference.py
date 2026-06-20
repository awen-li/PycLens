# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_free_reference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in self.executor.map(make_dummy_object, range(10)):
        wr = weakref.ref(obj)
        del obj
        support.gc_collect()
        self.assertIsNone(wr())
