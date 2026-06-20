# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: ReadTests_test_read_until

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    want = [b'xxxmatchyyy']
    telnet = test_telnet(want)
    data = telnet.read_until(b'match')
    self.assertEqual(data, b'xxxmatch', msg=(telnet.cookedq, telnet.rawq, telnet.sock.reads))
    reads = [b'x' * 50, b'match', b'y' * 50]
    expect = b''.join(reads[:-1])
    telnet = test_telnet(reads)
    data = telnet.read_until(b'match')
    self.assertEqual(data, expect)
