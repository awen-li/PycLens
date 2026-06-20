# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: ExpectTests_test_expect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    want = [b'x' * 10, b'match', b'y' * 10]
    telnet = test_telnet(want)
    (_, _, data) = telnet.expect([b'match'])
    self.assertEqual(data, b''.join(want[:-1]))
