# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel = cookies.Morsel()
    self.assertEqual(repr(morsel), '<Morsel: None=None>')
    self.assertEqual(str(morsel), 'Set-Cookie: None=None')
    morsel.set('key', 'val', 'coded_val')
    self.assertEqual(repr(morsel), '<Morsel: key=coded_val>')
    self.assertEqual(str(morsel), 'Set-Cookie: key=coded_val')
    morsel.update({'path': '/', 'comment': 'foo', 'domain': 'example.com', 'max-age': 0, 'secure': 0, 'version': 1})
    self.assertEqual(repr(morsel), '<Morsel: key=coded_val; Comment=foo; Domain=example.com; Max-Age=0; Path=/; Version=1>')
    self.assertEqual(str(morsel), 'Set-Cookie: key=coded_val; Comment=foo; Domain=example.com; Max-Age=0; Path=/; Version=1')
    morsel['secure'] = True
    morsel['httponly'] = 1
    self.assertEqual(repr(morsel), '<Morsel: key=coded_val; Comment=foo; Domain=example.com; HttpOnly; Max-Age=0; Path=/; Secure; Version=1>')
    self.assertEqual(str(morsel), 'Set-Cookie: key=coded_val; Comment=foo; Domain=example.com; HttpOnly; Max-Age=0; Path=/; Secure; Version=1')
    morsel = cookies.Morsel()
    morsel.set('key', 'val', 'coded_val')
    morsel['expires'] = 0
    self.assertRegex(repr(morsel), '<Morsel: key=coded_val; expires=\\w+, \\d+ \\w+ \\d+ \\d+:\\d+:\\d+ \\w+>')
    self.assertRegex(str(morsel), 'Set-Cookie: key=coded_val; expires=\\w+, \\d+ \\w+ \\d+ \\d+:\\d+:\\d+ \\w+')
