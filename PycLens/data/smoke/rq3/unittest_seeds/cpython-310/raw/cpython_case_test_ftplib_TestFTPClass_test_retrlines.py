# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_retrlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    received = []
    self.client.retrlines('retr', received.append)
    self.check_data(''.join(received), RETR_DATA.replace('\r\n', ''))
