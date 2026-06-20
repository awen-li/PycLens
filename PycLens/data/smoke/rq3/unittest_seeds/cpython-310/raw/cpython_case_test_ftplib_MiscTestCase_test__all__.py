# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: MiscTestCase_test__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_exported = {'MSG_OOB', 'FTP_PORT', 'MAXLINE', 'CRLF', 'B_CRLF', 'Error', 'parse150', 'parse227', 'parse229', 'parse257', 'print_line', 'ftpcp', 'test'}
    support.check__all__(self, ftplib, not_exported=not_exported)
