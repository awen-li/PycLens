# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: TestMailOptionParsing_test_with_decode_data_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = DummyServer((socket_helper.HOST, 0), ('b', 0), decode_data=True)
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr, decode_data=True)
    self.write_line(channel, b'EHLO example')
    for line in [b'MAIL from: <foo@example.com> size=20 SMTPUTF8', b'MAIL from: <foo@example.com> size=20 SMTPUTF8 BODY=8BITMIME', b'MAIL from: <foo@example.com> size=20 BODY=UNKNOWN', b'MAIL from: <foo@example.com> size=20 body=8bitmime']:
        self.write_line(channel, line)
        self.assertEqual(channel.socket.last, self.error_response)
    self.write_line(channel, b'MAIL from: <foo@example.com> size=20')
    self.assertEqual(channel.socket.last, b'250 OK\r\n')
