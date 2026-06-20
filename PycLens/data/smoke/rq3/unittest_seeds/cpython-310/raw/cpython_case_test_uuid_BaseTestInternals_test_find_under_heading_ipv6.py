# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestInternals_test_find_under_heading_ipv6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'Name    Mtu Network       Address              Ipkts Ierrs Idrop    Opkts Oerrs  Coll\nvtnet  1500 <Link#1>      52:54:00:9d:0e:67    10017     0     0     8174     0     0\nvtnet     - fe80::%vtnet0 fe80::5054:ff:fe9        0     -     -        4     -     -\nvtnet     - 192.168.122.0 192.168.122.45        8844     -     -     8171     -     -\nlo0   16384 <Link#2>      lo0                 260148     0     0   260148     0     0\nlo0       - ::1/128       ::1                    193     -     -      193     -     -\n                          ff01::1%lo0\n                          ff02::2:2eb7:74fa\n                          ff02::2:ff2e:b774\n                          ff02::1%lo0\n                          ff02::1:ff00:1%lo\nlo0       - fe80::%lo0/64 fe80::1%lo0              0     -     -        0     -     -\n                          ff01::1%lo0\n                          ff02::2:2eb7:74fa\n                          ff02::2:ff2e:b774\n                          ff02::1%lo0\n                          ff02::1:ff00:1%lo\nlo0       - 127.0.0.0/8   127.0.0.1           259955     -     -   259955     -     -\n                          224.0.0.1\n'
    with mock.patch.multiple(self.uuid, _MAC_DELIM=b':', _MAC_OMITS_LEADING_ZEROES=False, _get_command_stdout=mock_get_command_stdout(data)):
        mac = self.uuid._find_mac_under_heading(command='netstat', args='-ian', heading=b'Address')
    self.assertEqual(mac, 90520741023335)
