# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestFrame_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = traceback.FrameSummary('f', 1, 'dummy', line='line')
    self.assertEqual(len(f), 4)
