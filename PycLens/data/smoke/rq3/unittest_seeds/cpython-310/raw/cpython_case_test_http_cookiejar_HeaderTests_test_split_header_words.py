# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: HeaderTests_test_split_header_words

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [('foo', [[('foo', None)]]), ('foo=bar', [[('foo', 'bar')]]), ('   foo   ', [[('foo', None)]]), ('   foo=   ', [[('foo', '')]]), ('   foo=', [[('foo', '')]]), ('   foo=   ; ', [[('foo', '')]]), ('   foo=   ; bar= baz ', [[('foo', ''), ('bar', 'baz')]]), ('foo=bar bar=baz', [[('foo', 'bar'), ('bar', 'baz')]]), ('foo= bar=baz', [[('foo', 'bar=baz')]]), ('foo=bar;bar=baz', [[('foo', 'bar'), ('bar', 'baz')]]), ('foo bar baz', [[('foo', None), ('bar', None), ('baz', None)]]), ('a, b, c', [[('a', None)], [('b', None)], [('c', None)]]), ('foo; bar=baz, spam=, foo="\\,\\;\\"", bar= ', [[('foo', None), ('bar', 'baz')], [('spam', '')], [('foo', ',;"')], [('bar', '')]])]
    for (arg, expect) in tests:
        try:
            result = split_header_words([arg])
        except:
            import traceback, io
            f = io.StringIO()
            traceback.print_exc(None, f)
            result = '(error -- traceback follows)\n\n%s' % f.getvalue()
        self.assertEqual(result, expect, "\nWhen parsing: '%s'\nExpected:     '%s'\nGot:          '%s'\n" % (arg, expect, result))
