# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_send_message_error_on_non_ascii_addrs_if_no_smtputf8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = EmailMessage()
    msg['From'] = 'Páolo <főo@bar.com>'
    msg['To'] = 'Dinsdale'
    msg['Subject'] = 'Nudge nudge, wink, wink ὠ9'
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    with self.assertRaises(smtplib.SMTPNotSupportedError):
        smtp.send_message(msg)
