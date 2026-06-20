# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_exported = {'logfile', 'logfp', 'initlog', 'dolog', 'nolog', 'closelog', 'log', 'maxlen', 'valid_boundary'}
    support.check__all__(self, cgi, not_exported=not_exported)
