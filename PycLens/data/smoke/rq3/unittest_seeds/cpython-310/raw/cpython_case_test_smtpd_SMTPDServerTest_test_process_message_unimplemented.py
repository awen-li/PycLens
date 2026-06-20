# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDServerTest_test_process_message_unimplemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = smtpd.SMTPServer((socket_helper.HOST, 0), ('b', 0), decode_data=True)
    (conn, addr) = server.accept()
    channel = smtpd.SMTPChannel(server, conn, addr, decode_data=True)

    def write_line(line):
        channel.socket.queue_recv(line)
        channel.handle_read()
    write_line(b'HELO example')
    write_line(b'MAIL From:eggs@example')
    write_line(b'RCPT To:spam@example')
    write_line(b'DATA')
    self.assertRaises(NotImplementedError, write_line, b'spam\r\n.\r\n')
