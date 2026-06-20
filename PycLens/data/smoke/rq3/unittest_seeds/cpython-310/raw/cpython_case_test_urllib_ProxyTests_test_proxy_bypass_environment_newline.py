# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: ProxyTests_test_proxy_bypass_environment_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bypass = urllib.request.proxy_bypass_environment
    self.env.set('NO_PROXY', 'localhost, anotherdomain.com, newdomain.com:1234')
    self.assertFalse(bypass('localhost\n'))
    self.assertFalse(bypass('anotherdomain.com:8888\n'))
    self.assertFalse(bypass('newdomain.com:1234\n'))
