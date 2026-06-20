# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: TestMailOptionParsing_test_with_enable_smtputf8_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = DummyServer((socket_helper.HOST, 0), ('b', 0), enable_SMTPUTF8=True)
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr, enable_SMTPUTF8=True)
    self.write_line(channel, b'EHLO example')
    self.write_line(channel, b'MAIL from: <foo@example.com> size=20 body=8bitmime smtputf8')
    self.assertEqual(channel.socket.last, b'250 OK\r\n')
