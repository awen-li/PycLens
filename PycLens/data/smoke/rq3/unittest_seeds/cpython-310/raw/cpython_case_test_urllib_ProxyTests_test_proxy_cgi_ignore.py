# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: ProxyTests_test_proxy_cgi_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        self.env.set('HTTP_PROXY', 'http://somewhere:3128')
        proxies = urllib.request.getproxies_environment()
        self.assertEqual('http://somewhere:3128', proxies['http'])
        self.env.set('REQUEST_METHOD', 'GET')
        proxies = urllib.request.getproxies_environment()
        self.assertNotIn('http', proxies)
    finally:
        self.env.unset('REQUEST_METHOD')
        self.env.unset('HTTP_PROXY')
