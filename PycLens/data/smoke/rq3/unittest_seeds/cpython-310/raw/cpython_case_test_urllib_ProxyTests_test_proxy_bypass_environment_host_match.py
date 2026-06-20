# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: ProxyTests_test_proxy_bypass_environment_host_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bypass = urllib.request.proxy_bypass_environment
    self.env.set('NO_PROXY', 'localhost, anotherdomain.com, newdomain.com:1234, .d.o.t')
    self.assertTrue(bypass('localhost'))
    self.assertTrue(bypass('LocalHost'))
    self.assertTrue(bypass('LOCALHOST'))
    self.assertTrue(bypass('.localhost'))
    self.assertTrue(bypass('newdomain.com:1234'))
    self.assertTrue(bypass('.newdomain.com:1234'))
    self.assertTrue(bypass('foo.d.o.t'))
    self.assertTrue(bypass('d.o.t'))
    self.assertTrue(bypass('anotherdomain.com:8888'))
    self.assertTrue(bypass('.anotherdomain.com:8888'))
    self.assertTrue(bypass('www.newdomain.com:1234'))
    self.assertFalse(bypass('prelocalhost'))
    self.assertFalse(bypass('newdomain.com'))
    self.assertFalse(bypass('newdomain.com:1235'))
