# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPUTF8SimTests_test_send_message_uses_smtputf8_if_addrs_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = EmailMessage()
    msg['From'] = 'Páolo <főo@bar.com>'
    msg['To'] = 'Dinsdale'
    msg['Subject'] = 'Nudge nudge, wink, wink ὠ9'
    msg.set_content('oh là là, know what I mean, know what I mean?\n\n')
    expected = textwrap.dedent('            From: Páolo <főo@bar.com>\n            To: Dinsdale\n            Subject: Nudge nudge, wink, wink ὠ9\n            Content-Type: text/plain; charset="utf-8"\n            Content-Transfer-Encoding: 8bit\n            MIME-Version: 1.0\n\n            oh là là, know what I mean, know what I mean?\n            ')
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    self.assertEqual(smtp.send_message(msg), {})
    self.assertEqual(self.serv.last_mailfrom, 'főo@bar.com')
    self.assertEqual(self.serv.last_rcpttos, ['Dinsdale'])
    self.assertEqual(self.serv.last_message.decode(), expected)
    self.assertIn('BODY=8BITMIME', self.serv.last_mail_options)
    self.assertIn('SMTPUTF8', self.serv.last_mail_options)
    self.assertEqual(self.serv.last_rcpt_options, [])
