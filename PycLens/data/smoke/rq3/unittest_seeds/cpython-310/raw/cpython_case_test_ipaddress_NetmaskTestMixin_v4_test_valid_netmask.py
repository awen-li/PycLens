# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v4_test_valid_netmask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(self.factory(('192.0.2.0', 24))), '192.0.2.0/24')
    self.assertEqual(str(self.factory(('192.0.2.0', '24'))), '192.0.2.0/24')
    self.assertEqual(str(self.factory(('192.0.2.0', '255.255.255.0'))), '192.0.2.0/24')
    self.assertEqual(str(self.factory('192.0.2.0/255.255.255.0')), '192.0.2.0/24')
    for i in range(0, 33):
        net_str = '0.0.0.0/%d' % i
        net = self.factory(net_str)
        self.assertEqual(str(net), net_str)
        self.assertEqual(str(self.factory('0.0.0.0/%s' % net.netmask)), net_str)
        self.assertEqual(str(self.factory('0.0.0.0/0%d' % i)), net_str)
        if i in (32, 0):
            net_str = '0.0.0.0/%d' % (32 - i)
        self.assertEqual(str(self.factory('0.0.0.0/%s' % net.hostmask)), net_str)
