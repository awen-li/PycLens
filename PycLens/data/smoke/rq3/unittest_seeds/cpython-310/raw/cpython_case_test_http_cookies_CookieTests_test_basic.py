# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [{'data': 'chips=ahoy; vienna=finger', 'dict': {'chips': 'ahoy', 'vienna': 'finger'}, 'repr': "<SimpleCookie: chips='ahoy' vienna='finger'>", 'output': 'Set-Cookie: chips=ahoy\nSet-Cookie: vienna=finger'}, {'data': 'keebler="E=mc2; L=\\"Loves\\"; fudge=\\012;"', 'dict': {'keebler': 'E=mc2; L="Loves"; fudge=\n;'}, 'repr': '<SimpleCookie: keebler=\'E=mc2; L="Loves"; fudge=\\n;\'>', 'output': 'Set-Cookie: keebler="E=mc2; L=\\"Loves\\"; fudge=\\012;"'}, {'data': 'keebler=E=mc2', 'dict': {'keebler': 'E=mc2'}, 'repr': "<SimpleCookie: keebler='E=mc2'>", 'output': 'Set-Cookie: keebler=E=mc2'}, {'data': 'key:term=value:term', 'dict': {'key:term': 'value:term'}, 'repr': "<SimpleCookie: key:term='value:term'>", 'output': 'Set-Cookie: key:term=value:term'}, {'data': 'a=b; c=[; d=r; f=h', 'dict': {'a': 'b', 'c': '[', 'd': 'r', 'f': 'h'}, 'repr': "<SimpleCookie: a='b' c='[' d='r' f='h'>", 'output': '\n'.join(('Set-Cookie: a=b', 'Set-Cookie: c=[', 'Set-Cookie: d=r', 'Set-Cookie: f=h'))}]
    for case in cases:
        C = cookies.SimpleCookie()
        C.load(case['data'])
        self.assertEqual(repr(C), case['repr'])
        self.assertEqual(C.output(sep='\n'), case['output'])
        for (k, v) in sorted(case['dict'].items()):
            self.assertEqual(C[k].value, v)
