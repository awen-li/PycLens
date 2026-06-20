# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolExecutorTest_test_hang_global_shutdown_lock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def submit(pool):
        pool.submit(submit, pool)
    with futures.ThreadPoolExecutor(1) as pool:
        pool.submit(submit, pool)
        for _ in range(50):
            with futures.ProcessPoolExecutor(1, mp_context=mp.get_context('fork')) as workers:
                workers.submit(tuple)
