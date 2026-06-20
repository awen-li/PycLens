# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlopenNetworkTests_test_geturl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlopen(self.url) as open_url:
        gotten_url = open_url.geturl()
        self.assertEqual(gotten_url, self.url)
