# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_ftp_cache_pruning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakeftp()
    try:
        urllib.request.ftpcache['test'] = urllib.request.ftpwrapper('user', 'pass', 'localhost', 21, [])
        urlopen('ftp://localhost')
    finally:
        self.unfakeftp()
