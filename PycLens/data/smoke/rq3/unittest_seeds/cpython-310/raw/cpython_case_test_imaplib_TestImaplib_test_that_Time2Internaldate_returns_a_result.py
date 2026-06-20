# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: TestImaplib_test_that_Time2Internaldate_returns_a_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for t in self.timevalues():
        imaplib.Time2Internaldate(t)
