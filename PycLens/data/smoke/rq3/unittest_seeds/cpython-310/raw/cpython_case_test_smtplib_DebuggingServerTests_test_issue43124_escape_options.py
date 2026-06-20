# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: DebuggingServerTests_test_issue43124_escape_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = 'wazzuuup\nlinetwo'
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    smtp.sendmail('hi@me.com', 'you@me.com', m)
    with self.assertRaises(ValueError) as exc:
        smtp.mail('hi@me.com', ['X-OPTION\nX-INJECTED-1', 'X-OPTION2\nX-INJECTED-2'])
    msg = str(exc.exception)
    self.assertIn('prohibited newline characters', msg)
    self.assertIn('X-OPTION\\nX-INJECTED-1 X-OPTION2\\nX-INJECTED-2', msg)
    time.sleep(0.01)
    smtp.quit()
    debugout = smtpd.DEBUGSTREAM.getvalue()
    self.assertNotIn('X-OPTION', debugout)
    self.assertNotIn('X-OPTION2', debugout)
    self.assertNotIn('X-INJECTED-1', debugout)
    self.assertNotIn('X-INJECTED-2', debugout)
