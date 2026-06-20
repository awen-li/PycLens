# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: OptionTests_test_debuglevel_reads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given_a_expect_b = [(b'a', ": recv b''\n"), (tl.IAC + bytes([88]), ': IAC 88 not recognized\n'), (tl.IAC + tl.DO + bytes([1]), ': IAC DO 1\n'), (tl.IAC + tl.DONT + bytes([1]), ': IAC DONT 1\n'), (tl.IAC + tl.WILL + bytes([1]), ': IAC WILL 1\n'), (tl.IAC + tl.WONT + bytes([1]), ': IAC WONT 1\n')]
    for (a, b) in given_a_expect_b:
        telnet = test_telnet([a])
        telnet.set_debuglevel(1)
        txt = telnet.read_all()
        self.assertIn(b, telnet._messages)
    return
