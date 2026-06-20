# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlopenNetworkTests_test_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlopen(self.url) as open_url:
        self.assertIsInstance(open_url.readline(), bytes, 'readline did not return a string')
        self.assertIsInstance(open_url.readlines(), list, 'readlines did not return a list')
