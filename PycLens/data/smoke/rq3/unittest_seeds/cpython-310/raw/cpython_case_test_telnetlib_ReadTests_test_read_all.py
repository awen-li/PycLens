# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: ReadTests_test_read_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    reads = [b'x' * 500, b'y' * 500, b'z' * 500]
    expect = b''.join(reads)
    telnet = test_telnet(reads)
    data = telnet.read_all()
    self.assertEqual(data, expect)
    return
