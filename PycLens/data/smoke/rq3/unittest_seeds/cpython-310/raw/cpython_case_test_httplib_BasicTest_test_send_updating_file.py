# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_send_updating_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def data():
        yield 'data'
        yield None
        yield 'data_two'

    class UpdatingFile(io.TextIOBase):
        mode = 'r'
        d = data()

        def read(self, blocksize=-1):
            return next(self.d)
    expected = b'data'
    conn = client.HTTPConnection('example.com')
    sock = FakeSocket('')
    conn.sock = sock
    conn.send(UpdatingFile())
    self.assertEqual(sock.data, expected)
