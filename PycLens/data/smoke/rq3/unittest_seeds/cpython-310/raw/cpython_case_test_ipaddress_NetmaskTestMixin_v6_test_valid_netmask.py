# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v6_test_valid_netmask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(self.factory(('2001:db8::', 32))), '2001:db8::/32')
    self.assertEqual(str(self.factory(('2001:db8::', '32'))), '2001:db8::/32')
    self.assertEqual(str(self.factory('2001:db8::/32')), '2001:db8::/32')
    for i in range(0, 129):
        net_str = '::/%d' % i
        self.assertEqual(str(self.factory(net_str)), net_str)
        self.assertEqual(str(self.factory('::/0%d' % i)), net_str)
    self.assertEqual(str(self.factory('2001:db8::%scope/32')), '2001:db8::%scope/32')
    for i in range(0, 129):
        net_str = '::/%d' % i
        self.assertEqual(str(self.factory(net_str)), net_str)
        self.assertEqual(str(self.factory('::/0%d' % i)), net_str)
