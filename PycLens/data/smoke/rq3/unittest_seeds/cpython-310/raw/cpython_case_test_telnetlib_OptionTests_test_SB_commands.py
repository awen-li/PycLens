# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: OptionTests_test_SB_commands

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    send = [tl.IAC + tl.SB + tl.IAC + tl.SE, tl.IAC + tl.SB + tl.IAC + tl.IAC + tl.IAC + tl.SE, tl.IAC + tl.SB + tl.IAC + tl.IAC + b'aa' + tl.IAC + tl.SE, tl.IAC + tl.SB + b'bb' + tl.IAC + tl.IAC + tl.IAC + tl.SE, tl.IAC + tl.SB + b'cc' + tl.IAC + tl.IAC + b'dd' + tl.IAC + tl.SE]
    telnet = test_telnet(send)
    nego = nego_collector(telnet.read_sb_data)
    telnet.set_option_negotiation_callback(nego.do_nego)
    txt = telnet.read_all()
    self.assertEqual(txt, b'')
    want_sb_data = tl.IAC + tl.IAC + b'aabb' + tl.IAC + b'cc' + tl.IAC + b'dd'
    self.assertEqual(nego.sb_seen, want_sb_data)
    self.assertEqual(b'', telnet.read_sb_data())
    nego.sb_getter = None
