# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_with_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with smtplib.SMTP(HOST, self.port) as smtp:
        (code, message) = smtp.noop()
        self.assertEqual(code, 250)
    self.assertRaises(smtplib.SMTPServerDisconnected, smtp.send, b'foo')
    with smtplib.SMTP(HOST, self.port) as smtp:
        smtp.close()
    self.assertRaises(smtplib.SMTPServerDisconnected, smtp.send, b'foo')
