# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: AsCompletedTests_test_correct_timeout_exception_msg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    futures_list = [CANCELLED_AND_NOTIFIED_FUTURE, PENDING_FUTURE, RUNNING_FUTURE, SUCCESSFUL_FUTURE]
    with self.assertRaises(futures.TimeoutError) as cm:
        list(futures.as_completed(futures_list, timeout=0))
    self.assertEqual(str(cm.exception), '2 (of 4) futures unfinished')
