# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_chunked_missing_end

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = chunked_expected
    sock = FakeSocket(chunked_start + last_chunk)
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    self.assertEqual(resp.read(), expected)
    resp.close()
