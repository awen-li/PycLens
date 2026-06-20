# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_extract_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = traceback.StackSummary.extract(traceback.walk_stack(None))
    self.assertIsInstance(s, traceback.StackSummary)
