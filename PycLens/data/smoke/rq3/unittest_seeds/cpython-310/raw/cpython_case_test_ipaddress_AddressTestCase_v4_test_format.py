# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v4 = ipaddress.IPv4Address('1.2.3.42')
    v4_pairs = [('b', '00000001000000100000001100101010'), ('n', '00000001000000100000001100101010'), ('x', '0102032a'), ('X', '0102032A'), ('_b', '0000_0001_0000_0010_0000_0011_0010_1010'), ('_n', '0000_0001_0000_0010_0000_0011_0010_1010'), ('_x', '0102_032a'), ('_X', '0102_032A'), ('#b', '0b00000001000000100000001100101010'), ('#n', '0b00000001000000100000001100101010'), ('#x', '0x0102032a'), ('#X', '0X0102032A'), ('#_b', '0b0000_0001_0000_0010_0000_0011_0010_1010'), ('#_n', '0b0000_0001_0000_0010_0000_0011_0010_1010'), ('#_x', '0x0102_032a'), ('#_X', '0X0102_032A'), ('s', '1.2.3.42'), ('', '1.2.3.42')]
    for (fmt, txt) in v4_pairs:
        self.assertEqual(txt, format(v4, fmt))
