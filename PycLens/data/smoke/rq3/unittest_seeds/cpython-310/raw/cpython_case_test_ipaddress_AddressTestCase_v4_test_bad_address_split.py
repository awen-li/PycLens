# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_bad_address_split

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadSplit(addr):
        with self.assertAddressError('Expected 4 octets in %r', addr):
            ipaddress.IPv4Address(addr)
    assertBadSplit('127.0.1')
    assertBadSplit('42.42.42.42.42')
    assertBadSplit('42.42.42')
    assertBadSplit('42.42')
    assertBadSplit('42')
    assertBadSplit('42..42.42.42')
    assertBadSplit('42.42.42.42.')
    assertBadSplit('42.42.42.42...')
    assertBadSplit('.42.42.42.42')
    assertBadSplit('...42.42.42.42')
    assertBadSplit('016.016.016')
    assertBadSplit('016.016')
    assertBadSplit('016')
    assertBadSplit('000')
    assertBadSplit('0x0a.0x0a.0x0a')
    assertBadSplit('0x0a.0x0a')
    assertBadSplit('0x0a')
    assertBadSplit('.')
    assertBadSplit('bogus')
    assertBadSplit('bogus.com')
    assertBadSplit('1000')
    assertBadSplit('1000000000000000')
    assertBadSplit('192.168.0.1.com')
