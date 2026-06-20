# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: DebuggingServerTest_test_process_SMTPUTF8_message_with_enable_SMTPUTF8_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = smtpd.DebuggingServer((socket_helper.HOST, 0), ('b', 0), enable_SMTPUTF8=True)
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr, enable_SMTPUTF8=True)
    with support.captured_stdout() as s:
        self.send_data(channel, b'From: test\n\nh\xc3\xa9llo\xff\n', enable_SMTPUTF8=True)
    stdout = s.getvalue()
    self.assertEqual(stdout, textwrap.dedent("             ---------- MESSAGE FOLLOWS ----------\n             mail options: ['BODY=8BITMIME', 'SMTPUTF8']\n             b'From: test'\n             b'X-Peer: peer-address'\n             b''\n             b'h\\xc3\\xa9llo\\xff'\n             ------------ END MESSAGE ------------\n             "))
