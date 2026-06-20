# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: ReadTests_test_read_some

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    telnet = test_telnet([b'x' * 500])
    data = telnet.read_some()
    self.assertTrue(len(data) >= 1)
    telnet = test_telnet()
    data = telnet.read_some()
    self.assertEqual(b'', data)
