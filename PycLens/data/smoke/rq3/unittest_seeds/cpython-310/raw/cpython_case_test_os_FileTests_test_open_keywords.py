# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_open_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = os.open(path=__file__, flags=os.O_RDONLY, mode=511, dir_fd=None)
    os.close(f)
