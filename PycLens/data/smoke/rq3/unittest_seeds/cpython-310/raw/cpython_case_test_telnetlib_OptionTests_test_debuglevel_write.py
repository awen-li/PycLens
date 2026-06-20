# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: OptionTests_test_debuglevel_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    telnet = test_telnet()
    telnet.set_debuglevel(1)
    telnet.write(b'xxx')
    expected = "send b'xxx'\n"
    self.assertIn(expected, telnet._messages)
