# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCAPI_test_untrack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.start()
    self.track()
    self.assertIsNotNone(self.get_traceback())
    self.assertEqual(self.get_traced_memory(), self.size)
    self.untrack()
    self.assertIsNone(self.get_traceback())
    self.assertEqual(self.get_traced_memory(), 0)
    self.untrack()
    self.untrack()
