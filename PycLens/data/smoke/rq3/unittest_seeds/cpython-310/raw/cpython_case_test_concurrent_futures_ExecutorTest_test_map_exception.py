# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_map_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.executor.map(divmod, [1, 1, 1, 1], [2, 3, 0, 5])
    self.assertEqual(i.__next__(), (0, 1))
    self.assertEqual(i.__next__(), (0, 1))
    self.assertRaises(ZeroDivisionError, i.__next__)
