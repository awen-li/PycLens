# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_check_c_globals.py
# case: ActualChecks_test_check_c_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        main('check', {})
    except NotImplementedError:
        raise unittest.SkipTest('not supported on this host')
