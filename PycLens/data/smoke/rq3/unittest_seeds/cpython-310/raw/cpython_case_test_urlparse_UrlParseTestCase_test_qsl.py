# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_qsl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (orig, expect) in parse_qsl_test_cases:
        result = urllib.parse.parse_qsl(orig, keep_blank_values=True)
        self.assertEqual(result, expect, 'Error parsing %r' % orig)
        expect_without_blanks = [v for v in expect if len(v[1])]
        result = urllib.parse.parse_qsl(orig, keep_blank_values=False)
        self.assertEqual(result, expect_without_blanks, 'Error parsing %r' % orig)
