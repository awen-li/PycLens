# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolExecutorTest_test_ressources_gced_in_workers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mgr = self.get_context().Manager()
    obj = EventfulGCObj(mgr)
    future = self.executor.submit(id, obj)
    future.result()
    self.assertTrue(obj.event.wait(timeout=1))
    obj = None
    support.gc_collect()
    mgr.shutdown()
    mgr.join()
