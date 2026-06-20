# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: AsCompletedTests_test_free_reference_yielded_future

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    futures_list = [Future() for _ in range(8)]
    futures_list.append(create_future(state=CANCELLED_AND_NOTIFIED))
    futures_list.append(create_future(state=FINISHED, result=42))
    with self.assertRaises(futures.TimeoutError):
        for future in futures.as_completed(futures_list, timeout=0):
            futures_list.remove(future)
            wr = weakref.ref(future)
            del future
            support.gc_collect()
            self.assertIsNone(wr())
    futures_list[0].set_result('test')
    for future in futures.as_completed(futures_list):
        futures_list.remove(future)
        wr = weakref.ref(future)
        del future
        support.gc_collect()
        self.assertIsNone(wr())
        if futures_list:
            futures_list[0].set_result('test')
