# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: OtherNetworkTests_test_urlwithfrag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    urlwith_frag = 'http://www.pythontest.net/index.html#frag'
    with socket_helper.transient_internet(urlwith_frag):
        req = urllib.request.Request(urlwith_frag)
        res = urllib.request.urlopen(req)
        self.assertEqual(res.geturl(), 'http://www.pythontest.net/index.html#frag')
