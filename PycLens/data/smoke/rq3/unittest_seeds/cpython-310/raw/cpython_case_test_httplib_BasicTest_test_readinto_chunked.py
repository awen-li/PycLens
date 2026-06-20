# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_readinto_chunked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = chunked_expected
    nexpected = len(expected)
    b = bytearray(128)
    sock = FakeSocket(chunked_start + last_chunk + chunked_end)
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    n = resp.readinto(b)
    self.assertEqual(b[:nexpected], expected)
    self.assertEqual(n, nexpected)
    resp.close()
    for n in range(1, 12):
        sock = FakeSocket(chunked_start + last_chunk + chunked_end)
        resp = client.HTTPResponse(sock, method='GET')
        resp.begin()
        m = memoryview(b)
        i = resp.readinto(m[0:n])
        i += resp.readinto(m[i:n + i])
        i += resp.readinto(m[i:])
        self.assertEqual(b[:nexpected], expected)
        self.assertEqual(i, nexpected)
        resp.close()
    for x in ('', 'foo\r\n'):
        sock = FakeSocket(chunked_start + x)
        resp = client.HTTPResponse(sock, method='GET')
        resp.begin()
        try:
            n = resp.readinto(b)
        except client.IncompleteRead as i:
            self.assertEqual(i.partial, expected)
            expected_message = 'IncompleteRead(%d bytes read)' % len(expected)
            self.assertEqual(repr(i), expected_message)
            self.assertEqual(str(i), expected_message)
        else:
            self.fail('IncompleteRead expected')
        finally:
            resp.close()
