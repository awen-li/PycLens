# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: TrivialTests_test_parse_http_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [('a,b,c', ['a', 'b', 'c']), ('path"o,l"og"i"cal, example', ['path"o,l"og"i"cal', 'example']), ('a, b, "c", "d", "e,f", g, h', ['a', 'b', '"c"', '"d"', '"e,f"', 'g', 'h']), ('a="b\\"c", d="e\\,f", g="h\\\\i"', ['a="b"c"', 'd="e,f"', 'g="h\\i"'])]
    for (string, list) in tests:
        self.assertEqual(urllib.request.parse_http_list(string), list)
