# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: ProxyTests_test_proxy_bypass_environment_always_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bypass = urllib.request.proxy_bypass_environment
    self.env.set('NO_PROXY', '*')
    self.assertTrue(bypass('newdomain.com'))
    self.assertTrue(bypass('newdomain.com:1234'))
    self.env.set('NO_PROXY', '*, anotherdomain.com')
    self.assertTrue(bypass('anotherdomain.com'))
    self.assertFalse(bypass('newdomain.com'))
    self.assertFalse(bypass('newdomain.com:1234'))
