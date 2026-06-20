# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_walk_tb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except Exception:
        (_, _, tb) = sys.exc_info()
    s = list(traceback.walk_tb(tb))
    self.assertEqual(len(s), 1)
