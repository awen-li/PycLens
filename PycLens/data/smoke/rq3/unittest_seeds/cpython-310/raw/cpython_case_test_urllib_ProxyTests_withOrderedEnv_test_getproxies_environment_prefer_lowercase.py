# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: ProxyTests_withOrderedEnv_test_getproxies_environment_prefer_lowercase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.environ['no_proxy'] = ''
    os.environ['No_Proxy'] = 'localhost'
    self.assertFalse(urllib.request.proxy_bypass_environment('localhost'))
    self.assertFalse(urllib.request.proxy_bypass_environment('arbitrary'))
    os.environ['http_proxy'] = ''
    os.environ['HTTP_PROXY'] = 'http://somewhere:3128'
    proxies = urllib.request.getproxies_environment()
    self.assertEqual({}, proxies)
    os.environ['no_proxy'] = 'localhost, noproxy.com, my.proxy:1234'
    os.environ['No_Proxy'] = 'xyz.com'
    self.assertTrue(urllib.request.proxy_bypass_environment('localhost'))
    self.assertTrue(urllib.request.proxy_bypass_environment('noproxy.com:5678'))
    self.assertTrue(urllib.request.proxy_bypass_environment('my.proxy:1234'))
    self.assertFalse(urllib.request.proxy_bypass_environment('my.proxy'))
    self.assertFalse(urllib.request.proxy_bypass_environment('arbitrary'))
    os.environ['http_proxy'] = 'http://somewhere:3128'
    os.environ['Http_Proxy'] = 'http://somewhereelse:3128'
    proxies = urllib.request.getproxies_environment()
    self.assertEqual('http://somewhere:3128', proxies['http'])
