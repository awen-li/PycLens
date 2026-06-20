# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_chunked_extension

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    extra = '3;foo=bar\r\n' + 'abc\r\n'
    expected = chunked_expected + b'abc'
    sock = FakeSocket(chunked_start + extra + last_chunk_extended + chunked_end)
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    self.assertEqual(resp.read(), expected)
    resp.close()
