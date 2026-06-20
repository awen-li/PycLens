# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: ProxyTests_test_getproxies_environment_keep_no_proxies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.env.set('NO_PROXY', 'localhost')
    proxies = urllib.request.getproxies_environment()
    self.assertEqual('localhost', proxies['no'])
    self.env.set('NO_PROXY', 'localhost, anotherdomain.com, newdomain.com:1234')
    self.assertTrue(urllib.request.proxy_bypass_environment('anotherdomain.com'))
    self.assertTrue(urllib.request.proxy_bypass_environment('anotherdomain.com:8888'))
    self.assertTrue(urllib.request.proxy_bypass_environment('newdomain.com:1234'))
