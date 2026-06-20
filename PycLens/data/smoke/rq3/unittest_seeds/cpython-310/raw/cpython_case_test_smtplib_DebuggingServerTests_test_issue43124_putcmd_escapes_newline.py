# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: DebuggingServerTests_test_issue43124_putcmd_escapes_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    with self.assertRaises(ValueError) as exc:
        smtp.putcmd('helo\nX-INJECTED')
    self.assertIn('prohibited newline characters', str(exc.exception))
    smtp.quit()
