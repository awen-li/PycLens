# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: PersistenceTest_test_disconnected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def make_reset_reader(text):
        """Return BufferedReader that raises ECONNRESET at EOF"""
        stream = io.BytesIO(text)

        def readinto(buffer):
            size = io.BytesIO.readinto(stream, buffer)
            if size == 0:
                raise ConnectionResetError()
            return size
        stream.readinto = readinto
        return io.BufferedReader(stream)
    tests = ((io.BytesIO, client.RemoteDisconnected), (make_reset_reader, ConnectionResetError))
    for (stream_factory, exception) in tests:
        with self.subTest(exception=exception):
            conn = FakeSocketHTTPConnection(b'', stream_factory)
            conn.request('GET', '/eof-response')
            self.assertRaises(exception, conn.getresponse)
            self.assertIsNone(conn.sock)
            conn.request('GET', '/reconnect')
            self.assertEqual(conn.connections, 2)
