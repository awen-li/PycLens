# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTestWithEnableSMTPUTF8True_test_process_smtputf8_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    for mail_parameters in [b'', b'BODY=8BITMIME SMTPUTF8']:
        self.write_line(b'MAIL from: <a@example> ' + mail_parameters)
        self.assertEqual(self.channel.socket.last[0:3], b'250')
        self.write_line(b'rcpt to:<b@example.com>')
        self.assertEqual(self.channel.socket.last[0:3], b'250')
        self.write_line(b'data')
        self.assertEqual(self.channel.socket.last[0:3], b'354')
        self.write_line(b'c\r\n.')
        if mail_parameters == b'':
            self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
        else:
            self.assertEqual(self.channel.socket.last, b'250 SMTPUTF8 message okish\r\n')
