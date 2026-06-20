# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_all_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exceptions = (ftplib.error_reply, ftplib.error_temp, ftplib.error_perm, ftplib.error_proto, ftplib.Error, OSError, EOFError)
    for x in exceptions:
        try:
            raise x('exception not included in all_errors set')
        except ftplib.all_errors:
            pass
