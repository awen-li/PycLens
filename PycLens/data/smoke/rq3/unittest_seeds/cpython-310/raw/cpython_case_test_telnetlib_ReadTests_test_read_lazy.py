# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: ReadTests_test_read_lazy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    want = b'x' * 100
    telnet = test_telnet([want])
    self.assertEqual(b'', telnet.read_lazy())
    data = b''
    while True:
        try:
            read_data = telnet.read_lazy()
            data += read_data
            if not read_data:
                telnet.fill_rawq()
        except EOFError:
            break
        self.assertTrue(want.startswith(data))
    self.assertEqual(data, want)
