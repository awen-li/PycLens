# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_escape_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [('/foo%2f/bar', '/foo%2F/bar'), ('/foo%2F/bar', '/foo%2F/bar'), ('/foo%%/bar', '/foo%%/bar'), ('/fo%19o/bar', '/fo%19o/bar'), ('/fo%7do/bar', '/fo%7Do/bar'), ('/foo/bar&', '/foo/bar&'), ('/foo//bar', '/foo//bar'), ('~/foo/bar', '~/foo/bar'), ('/foo\x19/bar', '/foo%19/bar'), ('/}foo/bar', '/%7Dfoo/bar'), ('/foo/barü', '/foo/bar%C3%BC'), ('/foo/barꯍ', '/foo/bar%EA%AF%8D')]
    for (arg, result) in cases:
        self.assertEqual(escape_path(arg), result)
