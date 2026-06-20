# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v6_test_netmask_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadNetmask(addr, netmask):
        msg = '%r is not a valid netmask' % netmask
        with self.assertNetmaskError(re.escape(msg)):
            self.factory('%s/%s' % (addr, netmask))
    assertBadNetmask('::1', '')
    assertBadNetmask('::1', '::1')
    assertBadNetmask('::1', '1::')
    assertBadNetmask('::1', '-1')
    assertBadNetmask('::1', '+1')
    assertBadNetmask('::1', ' 1 ')
    assertBadNetmask('::1', '0x1')
    assertBadNetmask('::1', '129')
    assertBadNetmask('::1', '1.2.3.4')
    assertBadNetmask('::1', 'pudding')
    assertBadNetmask('::', '::')
    assertBadNetmask('::1%scope', 'pudding')
