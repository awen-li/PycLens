# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: HeaderTests_test_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [('foo', 'foo'), ('foo=bar', 'foo=bar'), ('   foo   ', 'foo'), ('foo=', 'foo=""'), ('foo=bar bar=baz', 'foo=bar; bar=baz'), ('foo=bar;bar=baz', 'foo=bar; bar=baz'), ('foo bar baz', 'foo; bar; baz'), ('foo="\\"" bar="\\\\"', 'foo="\\""; bar="\\\\"'), ('foo,,,bar', 'foo, bar'), ('foo=bar,bar=baz', 'foo=bar, bar=baz'), ('text/html; charset=iso-8859-1', 'text/html; charset="iso-8859-1"'), ('foo="bar"; port="80,81"; discard, bar=baz', 'foo=bar; port="80,81"; discard, bar=baz'), ('Basic realm="\\"foo\\\\\\\\bar\\""', 'Basic; realm="\\"foo\\\\\\\\bar\\""')]
    for (arg, expect) in tests:
        input = split_header_words([arg])
        res = join_header_words(input)
        self.assertEqual(res, expect, "\nWhen parsing: '%s'\nExpected:     '%s'\nGot:          '%s'\nInput was:    '%s'\n" % (arg, expect, res, input))
