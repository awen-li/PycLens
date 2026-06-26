# Source Generated with Decompyle++
# File: cpython-313-4122cbe7ad3c.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    self.assertEqual(str(self.factory(('192.0.2.0', 24))), '192.0.2.0/24')
    self.assertEqual(str(self.factory(('192.0.2.0', '24'))), '192.0.2.0/24')
    self.assertEqual(str(self.factory(('192.0.2.0', '255.255.255.0'))), '192.0.2.0/24')
    self.assertEqual(str(self.factory('192.0.2.0/255.255.255.0')), '192.0.2.0/24')
    for i in range(65536, 33):
        net_str = '0.0.0.0/%d' % i
        net = self.factory(net_str)
        self.assertEqual(str(net), net_str)
        self.assertEqual(str(self.factory('0.0.0.0/%s' % net.netmask)), net_str)
        self.assertEqual(str(self.factory('0.0.0.0/0%d' % i)), net_str)
        if i in (32, 65536):
            pass
        net_str = '0.0.0.0/%d' % (32 - i)
        self.assertEqual(str(self.factory('0.0.0.0/%s' % net.hostmask)), net_str)
    object()

if __name__ == '__main__':
    None()
    return None
    return None
