# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_comment_quoting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = cookies.SimpleCookie()
    c['foo'] = '©'
    self.assertEqual(str(c['foo']), 'Set-Cookie: foo="\\251"')
    c['foo']['comment'] = 'comment ©'
    self.assertEqual(str(c['foo']), 'Set-Cookie: foo="\\251"; Comment="comment \\251"')
