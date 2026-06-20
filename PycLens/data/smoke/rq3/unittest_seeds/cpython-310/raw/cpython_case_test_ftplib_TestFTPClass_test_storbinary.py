# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_storbinary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO(RETR_DATA.encode(self.client.encoding))
    self.client.storbinary('stor', f)
    self.check_data(self.server.handler_instance.last_received_data, RETR_DATA)
    flag = []
    f.seek(0)
    self.client.storbinary('stor', f, callback=lambda x: flag.append(None))
    self.assertTrue(flag)
