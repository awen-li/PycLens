# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_with_statement_QUIT_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(smtplib.SMTPResponseException) as error:
        with smtplib.SMTP(HOST, self.port) as smtp:
            smtp.noop()
            self.serv._SMTPchannel.quit_response = '421 QUIT FAILED'
    self.assertEqual(error.exception.smtp_code, 421)
    self.assertEqual(error.exception.smtp_error, b'QUIT FAILED')
