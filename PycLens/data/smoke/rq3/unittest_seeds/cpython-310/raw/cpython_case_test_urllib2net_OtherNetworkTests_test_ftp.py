# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: OtherNetworkTests_test_ftp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    urls = ['ftp://www.pythontest.net/README', ('ftp://www.pythontest.net/non-existent-file', None, urllib.error.URLError)]
    self._test_urls(urls, self._extra_handlers())
