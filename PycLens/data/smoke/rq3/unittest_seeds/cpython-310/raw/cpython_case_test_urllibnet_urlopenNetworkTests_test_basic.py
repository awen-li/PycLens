# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlopenNetworkTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlopen(self.url) as open_url:
        for attr in ('read', 'readline', 'readlines', 'fileno', 'close', 'info', 'geturl'):
            self.assertTrue(hasattr(open_url, attr), 'object returned from urlopen lacks the %s attribute' % attr)
        self.assertTrue(open_url.read(), "calling 'read' failed")
