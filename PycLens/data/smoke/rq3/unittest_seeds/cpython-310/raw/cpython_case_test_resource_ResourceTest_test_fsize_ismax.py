# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_fsize_ismax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        (cur, max) = resource.getrlimit(resource.RLIMIT_FSIZE)
    except AttributeError:
        pass
    else:
        self.assertEqual(resource.RLIM_INFINITY, max)
        resource.setrlimit(resource.RLIMIT_FSIZE, (cur, max))
