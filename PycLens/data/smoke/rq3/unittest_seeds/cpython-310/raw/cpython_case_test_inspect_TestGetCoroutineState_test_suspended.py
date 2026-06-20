# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetCoroutineState_test_suspended

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.coroutine.send(None)
    self.assertEqual(self._coroutinestate(), inspect.CORO_SUSPENDED)
