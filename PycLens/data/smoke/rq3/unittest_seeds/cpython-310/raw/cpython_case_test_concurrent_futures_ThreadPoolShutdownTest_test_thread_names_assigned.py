# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolShutdownTest_test_thread_names_assigned

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = futures.ThreadPoolExecutor(max_workers=5, thread_name_prefix='SpecialPool')
    executor.map(abs, range(-5, 5))
    threads = executor._threads
    del executor
    support.gc_collect()
    for t in threads:
        self.assertRegex(t.name, '^SpecialPool_[0-4]$')
        t.join()
