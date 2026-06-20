# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_send_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket('')
    with self.assertRaises(TypeError):
        conn.request('POST', 'test', conn)
