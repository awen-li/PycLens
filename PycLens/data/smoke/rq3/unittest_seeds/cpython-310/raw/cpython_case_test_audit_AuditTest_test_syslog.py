# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_syslog

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    syslog = import_helper.import_module('syslog')
    (returncode, events, stderr) = self.run_python('test_syslog')
    if returncode:
        self.fail(stderr)
    if support.verbose:
        print('Events:', *events, sep='\n  ')
    self.assertSequenceEqual(events, [('syslog.openlog', ' ', f'python 0 {syslog.LOG_USER}'), ('syslog.syslog', ' ', f'{syslog.LOG_INFO} test'), ('syslog.setlogmask', ' ', f'{syslog.LOG_DEBUG}'), ('syslog.closelog', '', ''), ('syslog.syslog', ' ', f'{syslog.LOG_INFO} test2'), ('syslog.openlog', ' ', f'audit-tests.py 0 {syslog.LOG_USER}'), ('syslog.openlog', ' ', f'audit-tests.py {syslog.LOG_NDELAY} {syslog.LOG_LOCAL0}'), ('syslog.openlog', ' ', f'None 0 {syslog.LOG_USER}'), ('syslog.closelog', '', '')])
