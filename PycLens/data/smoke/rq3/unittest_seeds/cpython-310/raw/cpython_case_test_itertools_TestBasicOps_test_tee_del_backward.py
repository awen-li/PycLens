# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_tee_del_backward

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (forward, backward) = tee(repeat(None, 20000000))
    try:
        any(forward)
        del backward
    except:
        del forward, backward
        raise
