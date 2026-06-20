# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ShutdownTest_test_no_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler0 = FakeHandler(0, self.called)
    handler1 = FakeHandler(1, self.called)
    handler2 = FakeHandler(2, self.called)
    handlers = map(logging.weakref.ref, [handler0, handler1, handler2])
    logging.shutdown(handlerList=list(handlers))
    expected = ['2 - acquire', '2 - flush', '2 - close', '2 - release', '1 - acquire', '1 - flush', '1 - close', '1 - release', '0 - acquire', '0 - flush', '0 - close', '0 - release']
    self.assertEqual(expected, self.called)
