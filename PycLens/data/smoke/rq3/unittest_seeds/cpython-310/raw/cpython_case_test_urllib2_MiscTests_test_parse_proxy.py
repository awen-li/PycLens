# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: MiscTests_test_parse_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parse_proxy_test_cases = [('proxy.example.com', (None, None, None, 'proxy.example.com')), ('proxy.example.com:3128', (None, None, None, 'proxy.example.com:3128')), ('proxy.example.com', (None, None, None, 'proxy.example.com')), ('proxy.example.com:3128', (None, None, None, 'proxy.example.com:3128')), ('joe:password@proxy.example.com', (None, 'joe', 'password', 'proxy.example.com')), ('joe:password@proxy.example.com:3128', (None, 'joe', 'password', 'proxy.example.com:3128')), ('http://proxy.example.com/', ('http', None, None, 'proxy.example.com')), ('http://proxy.example.com:3128/', ('http', None, None, 'proxy.example.com:3128')), ('http://joe:password@proxy.example.com/', ('http', 'joe', 'password', 'proxy.example.com')), ('http://joe:password@proxy.example.com:3128', ('http', 'joe', 'password', 'proxy.example.com:3128')), ('ftp://joe:password@proxy.example.com/rubbish:3128', ('ftp', 'joe', 'password', 'proxy.example.com')), ('http://joe:password@proxy.example.com', ('http', 'joe', 'password', 'proxy.example.com')), ('http://user/name:password@localhost:22', ('http', 'user/name', 'password', 'localhost:22')), ('http://username:pass/word@localhost:22', ('http', 'username', 'pass/word', 'localhost:22')), ('http://user/name:pass/word@localhost:22', ('http', 'user/name', 'pass/word', 'localhost:22'))]
    for (tc, expected) in parse_proxy_test_cases:
        self.assertEqual(_parse_proxy(tc), expected)
    (self.assertRaises(ValueError, _parse_proxy, 'file:/ftp.example.com'),)
