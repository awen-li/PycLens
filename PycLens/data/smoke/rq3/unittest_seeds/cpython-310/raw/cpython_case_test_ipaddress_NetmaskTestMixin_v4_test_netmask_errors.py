# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v4_test_netmask_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadNetmask(addr, netmask):
        msg = '%r is not a valid netmask' % netmask
        with self.assertNetmaskError(re.escape(msg)):
            self.factory('%s/%s' % (addr, netmask))
    assertBadNetmask('1.2.3.4', '')
    assertBadNetmask('1.2.3.4', '-1')
    assertBadNetmask('1.2.3.4', '+1')
    assertBadNetmask('1.2.3.4', ' 1 ')
    assertBadNetmask('1.2.3.4', '0x1')
    assertBadNetmask('1.2.3.4', '33')
    assertBadNetmask('1.2.3.4', '254.254.255.256')
    assertBadNetmask('1.2.3.4', '1.a.2.3')
    assertBadNetmask('1.1.1.1', '254.xyz.2.3')
    assertBadNetmask('1.1.1.1', '240.255.0.0')
    assertBadNetmask('1.1.1.1', '255.254.128.0')
    assertBadNetmask('1.1.1.1', '0.1.127.255')
    assertBadNetmask('1.1.1.1', 'pudding')
    assertBadNetmask('1.1.1.1', '::')
