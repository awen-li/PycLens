# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_submit_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future = self.executor.submit(mul, 2, y=8)
    self.assertEqual(16, future.result())
    future = self.executor.submit(capture, 1, self=2, fn=3)
    self.assertEqual(future.result(), ((1,), {'self': 2, 'fn': 3}))
    with self.assertRaises(TypeError):
        self.executor.submit(fn=capture, arg=1)
    with self.assertRaises(TypeError):
        self.executor.submit(arg=1)
