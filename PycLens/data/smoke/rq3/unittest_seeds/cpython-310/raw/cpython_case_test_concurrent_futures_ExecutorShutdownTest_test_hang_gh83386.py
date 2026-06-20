# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorShutdownTest_test_hang_gh83386

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.executor_type == futures.ProcessPoolExecutor:
        raise unittest.SkipTest('Hangs, see https://github.com/python/cpython/issues/83386')
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            from concurrent.futures import {executor_type}\n            from test.test_concurrent_futures import sleep_and_print\n            if __name__ == "__main__":\n                if {context!r}: multiprocessing.set_start_method({context!r})\n                t = {executor_type}(max_workers=3)\n                t.submit(sleep_and_print, 1.0, "apple")\n                t.shutdown(wait=False)\n            '.format(executor_type=self.executor_type.__name__, context=getattr(self, 'ctx', None)))
    self.assertFalse(err)
    self.assertEqual(out.strip(), b'apple')
