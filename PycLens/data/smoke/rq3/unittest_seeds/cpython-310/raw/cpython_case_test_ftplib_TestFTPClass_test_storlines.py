# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_storlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = RETR_DATA.replace('\r\n', '\n').encode(self.client.encoding)
    f = io.BytesIO(data)
    self.client.storlines('stor', f)
    self.check_data(self.server.handler_instance.last_received_data, RETR_DATA)
    flag = []
    f.seek(0)
    self.client.storlines('stor foo', f, callback=lambda x: flag.append(None))
    self.assertTrue(flag)
    f = io.StringIO(RETR_DATA.replace('\r\n', '\n'))
    with warnings_helper.check_warnings(('', BytesWarning), quiet=True):
        self.assertRaises(TypeError, self.client.storlines, 'stor foo', f)
