# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestInternals_test_find_under_heading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'Name  Mtu   Network     Address           Ipkts Ierrs    Opkts Oerrs  Coll\nen0   1500  link#2      fe.ad.c.1.23.4   1714807956     0 711348489     0     0\n                        01:00:5e:00:00:01\nen0   1500  192.168.129 x071             1714807956     0 711348489     0     0\n                        224.0.0.1\nen0   1500  192.168.90  x071             1714807956     0 711348489     0     0\n                        224.0.0.1\n'
    with mock.patch.multiple(self.uuid, _MAC_DELIM=b'.', _MAC_OMITS_LEADING_ZEROES=True, _get_command_stdout=mock_get_command_stdout(data)):
        mac = self.uuid._find_mac_under_heading(command='netstat', args='-ian', heading=b'Address')
    self.assertEqual(mac, 280019184198404)
