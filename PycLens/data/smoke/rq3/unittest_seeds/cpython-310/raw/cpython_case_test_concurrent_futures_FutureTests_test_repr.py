# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRegex(repr(PENDING_FUTURE), '<Future at 0x[0-9a-f]+ state=pending>')
    self.assertRegex(repr(RUNNING_FUTURE), '<Future at 0x[0-9a-f]+ state=running>')
    self.assertRegex(repr(CANCELLED_FUTURE), '<Future at 0x[0-9a-f]+ state=cancelled>')
    self.assertRegex(repr(CANCELLED_AND_NOTIFIED_FUTURE), '<Future at 0x[0-9a-f]+ state=cancelled>')
    self.assertRegex(repr(EXCEPTION_FUTURE), '<Future at 0x[0-9a-f]+ state=finished raised OSError>')
    self.assertRegex(repr(SUCCESSFUL_FUTURE), '<Future at 0x[0-9a-f]+ state=finished returned int>')
