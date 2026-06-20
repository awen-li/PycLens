# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolShutdownTest_test_cancel_futures_wait_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            from concurrent.futures import ThreadPoolExecutor\n            from test.test_concurrent_futures import sleep_and_print\n            if __name__ == "__main__":\n                t = ThreadPoolExecutor()\n                t.submit(sleep_and_print, .1, "apple")\n                t.shutdown(wait=False, cancel_futures=True)\n            ')
    self.assertFalse(err)
    self.assertEqual(out.strip(), b'apple')
