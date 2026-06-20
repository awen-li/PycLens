# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_rename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.rename('a', 'b')
    self.server.handler_instance.next_response = '200'
    self.assertRaises(ftplib.error_reply, self.client.rename, 'a', 'b')
