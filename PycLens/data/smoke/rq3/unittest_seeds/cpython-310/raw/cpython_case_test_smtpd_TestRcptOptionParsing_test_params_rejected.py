# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: TestRcptOptionParsing_test_params_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = DummyServer((socket_helper.HOST, 0), ('b', 0))
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr)
    self.write_line(channel, b'EHLO example')
    self.write_line(channel, b'MAIL from: <foo@example.com> size=20')
    self.write_line(channel, b'RCPT to: <foo@example.com> foo=bar')
    self.assertEqual(channel.socket.last, self.error_response)
