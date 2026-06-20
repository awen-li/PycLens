# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_mktime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for t in (-2, -1, 0, 1):
        try:
            tt = time.localtime(t)
        except (OverflowError, OSError):
            pass
        else:
            self.assertEqual(time.mktime(tt), t)
