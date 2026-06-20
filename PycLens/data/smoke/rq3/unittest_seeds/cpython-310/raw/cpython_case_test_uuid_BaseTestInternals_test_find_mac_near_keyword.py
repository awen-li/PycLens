# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestInternals_test_find_mac_near_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = '\nfake      Link encap:UNSPEC  hwaddr 00-00\ncscotun0  Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00\neth0      Link encap:Ethernet  HWaddr 12:34:56:78:90:ab\n'
    with mock.patch.multiple(self.uuid, _MAC_DELIM=b':', _MAC_OMITS_LEADING_ZEROES=False, _get_command_stdout=mock_get_command_stdout(data)):
        mac = self.uuid._find_mac_near_keyword(command='ifconfig', args='', keywords=[b'hwaddr'], get_word_index=lambda x: x + 1)
    self.assertEqual(mac, 20015998341291)
