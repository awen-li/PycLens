# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: DebuggingServerTest_test_process_message_with_decode_data_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = smtpd.DebuggingServer((socket_helper.HOST, 0), ('b', 0), decode_data=True)
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr, decode_data=True)
    with support.captured_stdout() as s:
        self.send_data(channel, b'From: test\n\nhello\n')
    stdout = s.getvalue()
    self.assertEqual(stdout, textwrap.dedent('             ---------- MESSAGE FOLLOWS ----------\n             From: test\n             X-Peer: peer-address\n\n             hello\n             ------------ END MESSAGE ------------\n             '))
