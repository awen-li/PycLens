# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_localtime_without_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lt0 = time.localtime()
    lt1 = time.localtime(None)
    t0 = time.mktime(lt0)
    t1 = time.mktime(lt1)
    self.assertAlmostEqual(t1, t0, delta=0.2)
