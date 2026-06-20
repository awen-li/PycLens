# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_request_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    req = urllib.request.Request('http://www.example.com/rheum/rhaponticum;foo=bar;sing=song?apples=pears&spam=eggs#ni')
    self.assertEqual(request_path(req), '/rheum/rhaponticum;foo=bar;sing=song')
    req = urllib.request.Request('http://www.example.com/rheum/rhaponticum?apples=pears&spam=eggs#ni')
    self.assertEqual(request_path(req), '/rheum/rhaponticum')
    req = urllib.request.Request('http://www.example.com')
    self.assertEqual(request_path(req), '/')
