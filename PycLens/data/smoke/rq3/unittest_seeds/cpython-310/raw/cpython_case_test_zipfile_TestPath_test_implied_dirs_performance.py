# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_implied_dirs_performance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = ['/'.join(string.ascii_lowercase + str(n)) for n in range(10000)]
    zipfile.CompleteDirs._implied_dirs(data)
