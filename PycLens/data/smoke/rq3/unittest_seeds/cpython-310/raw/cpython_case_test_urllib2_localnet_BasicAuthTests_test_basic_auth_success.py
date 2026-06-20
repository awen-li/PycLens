# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: BasicAuthTests_test_basic_auth_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ah = urllib.request.HTTPBasicAuthHandler()
    ah.add_password(self.REALM, self.server_url, self.USER, self.PASSWD)
    urllib.request.install_opener(urllib.request.build_opener(ah))
    try:
        self.assertTrue(urllib.request.urlopen(self.server_url))
    except urllib.error.HTTPError:
        self.fail('Basic auth failed for the url: %s' % self.server_url)
