# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_fsize_toobig

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    too_big = 10 ** 50
    try:
        (cur, max) = resource.getrlimit(resource.RLIMIT_FSIZE)
    except AttributeError:
        pass
    else:
        try:
            resource.setrlimit(resource.RLIMIT_FSIZE, (too_big, max))
        except (OverflowError, ValueError):
            pass
        try:
            resource.setrlimit(resource.RLIMIT_FSIZE, (max, too_big))
        except (OverflowError, ValueError):
            pass
