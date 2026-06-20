# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_storbinary_rest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = RETR_DATA.replace('\r\n', '\n').encode(self.client.encoding)
    f = io.BytesIO(data)
    for r in (30, '30'):
        f.seek(0)
        self.client.storbinary('stor', f, rest=r)
        self.assertEqual(self.server.handler_instance.rest, str(r))
