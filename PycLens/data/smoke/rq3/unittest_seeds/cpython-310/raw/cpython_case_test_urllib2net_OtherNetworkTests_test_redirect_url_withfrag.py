# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: OtherNetworkTests_test_redirect_url_withfrag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    redirect_url_with_frag = 'http://www.pythontest.net/redir/with_frag/'
    with socket_helper.transient_internet(redirect_url_with_frag):
        req = urllib.request.Request(redirect_url_with_frag)
        res = urllib.request.urlopen(req)
        self.assertEqual(res.geturl(), 'http://www.pythontest.net/elsewhere/#frag')
