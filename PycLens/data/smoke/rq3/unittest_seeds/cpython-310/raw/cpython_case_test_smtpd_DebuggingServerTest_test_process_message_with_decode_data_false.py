# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: DebuggingServerTest_test_process_message_with_decode_data_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = smtpd.DebuggingServer((socket_helper.HOST, 0), ('b', 0))
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr)
    with support.captured_stdout() as s:
        self.send_data(channel, b'From: test\n\nh\xc3\xa9llo\xff\n')
    stdout = s.getvalue()
    self.assertEqual(stdout, textwrap.dedent("             ---------- MESSAGE FOLLOWS ----------\n             b'From: test'\n             b'X-Peer: peer-address'\n             b''\n             b'h\\xc3\\xa9llo\\xff'\n             ------------ END MESSAGE ------------\n             "))
