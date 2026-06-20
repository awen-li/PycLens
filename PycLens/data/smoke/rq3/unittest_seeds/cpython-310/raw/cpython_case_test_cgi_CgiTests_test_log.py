# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_log

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cgi.log('Testing')
    cgi.logfp = StringIO()
    cgi.initlog('%s', 'Testing initlog 1')
    cgi.log('%s', 'Testing log 2')
    self.assertEqual(cgi.logfp.getvalue(), 'Testing initlog 1\nTesting log 2\n')
    if os.path.exists(os.devnull):
        cgi.logfp = None
        cgi.logfile = os.devnull
        cgi.initlog('%s', 'Testing log 3')
        self.addCleanup(cgi.closelog)
        cgi.log('Testing log 4')
