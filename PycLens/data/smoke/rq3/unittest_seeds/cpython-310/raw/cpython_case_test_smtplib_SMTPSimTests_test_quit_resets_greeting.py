# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_quit_resets_greeting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    (code, message) = smtp.ehlo()
    self.assertEqual(code, 250)
    self.assertIn('size', smtp.esmtp_features)
    smtp.quit()
    self.assertNotIn('size', smtp.esmtp_features)
    smtp.connect(HOST, self.port)
    self.assertNotIn('size', smtp.esmtp_features)
    smtp.ehlo_or_helo_if_needed()
    self.assertIn('size', smtp.esmtp_features)
    smtp.quit()
