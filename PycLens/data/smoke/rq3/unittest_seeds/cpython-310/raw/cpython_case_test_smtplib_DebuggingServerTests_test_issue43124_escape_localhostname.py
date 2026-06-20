# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: DebuggingServerTests_test_issue43124_escape_localhostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = 'wazzuuup\nlinetwo'
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='hi\nX-INJECTED', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    with self.assertRaises(ValueError) as exc:
        smtp.sendmail('hi@me.com', 'you@me.com', m)
    self.assertIn('prohibited newline characters: ehlo hi\\nX-INJECTED', str(exc.exception))
    time.sleep(0.01)
    smtp.quit()
    debugout = smtpd.DEBUGSTREAM.getvalue()
    self.assertNotIn('X-INJECTED', debugout)
