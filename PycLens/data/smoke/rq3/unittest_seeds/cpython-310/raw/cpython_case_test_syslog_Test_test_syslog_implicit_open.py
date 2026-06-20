# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syslog.py
# case: Test_test_syslog_implicit_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    syslog.closelog()
    syslog.syslog('test message from python test_syslog')
    syslog.syslog(syslog.LOG_ERR, 'test error from python test_syslog')
