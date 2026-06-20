# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: OptionTests_test_debug_accepts_str_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with test_socket([]):
        telnet = TelnetAlike('dummy', '0')
        telnet._messages = ''
    telnet.set_debuglevel(1)
    telnet.msg('test')
    self.assertRegex(telnet._messages, '0.*test')
