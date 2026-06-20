# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: WriteTests_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data_sample = [b'data sample without IAC', b'data sample with' + tl.IAC + b' one IAC', b'a few' + tl.IAC + tl.IAC + b' iacs' + tl.IAC, tl.IAC, b'']
    for data in data_sample:
        telnet = test_telnet()
        telnet.write(data)
        written = b''.join(telnet.sock.writes)
        self.assertEqual(data.replace(tl.IAC, tl.IAC + tl.IAC), written)
