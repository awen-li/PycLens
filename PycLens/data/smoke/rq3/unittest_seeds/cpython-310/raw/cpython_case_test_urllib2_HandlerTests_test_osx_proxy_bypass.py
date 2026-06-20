# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_osx_proxy_bypass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bypass = {'exclude_simple': False, 'exceptions': ['foo.bar', '*.bar.com', '127.0.0.1', '10.10', '10.0/16']}
    for host in ('foo.bar', 'www.bar.com', '127.0.0.1', '10.10.0.1', '10.0.0.1'):
        self.assertTrue(_proxy_bypass_macosx_sysconf(host, bypass), 'expected bypass of %s to be True' % host)
    for host in ('abc.foo.bar', 'bar.com', '127.0.0.2', '10.11.0.1', 'notinbypass'):
        self.assertFalse(_proxy_bypass_macosx_sysconf(host, bypass), 'expected bypass of %s to be False' % host)
    bypass = {'exclude_simple': True, 'exceptions': []}
    self.assertTrue(_proxy_bypass_macosx_sysconf('test', bypass))
    bypass = {'exclude_simple': False, 'exceptions': ['10.0.0.0/40', '172.19.10.0/24']}
    host = '172.19.10.5'
    self.assertTrue(_proxy_bypass_macosx_sysconf(host, bypass), 'expected bypass of %s to be True' % host)
    host = '10.0.1.5'
    self.assertFalse(_proxy_bypass_macosx_sysconf(host, bypass), 'expected bypass of %s to be False' % host)
