# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_reach

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(reach('www.acme.com'), '.acme.com')
    self.assertEqual(reach('acme.com'), 'acme.com')
    self.assertEqual(reach('acme.local'), '.local')
    self.assertEqual(reach('.local'), '.local')
    self.assertEqual(reach('.com'), '.com')
    self.assertEqual(reach('.'), '.')
    self.assertEqual(reach(''), '')
    self.assertEqual(reach('192.168.0.1'), '192.168.0.1')
