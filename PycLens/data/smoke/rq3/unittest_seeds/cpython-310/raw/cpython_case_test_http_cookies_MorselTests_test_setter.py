# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_setter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    M = cookies.Morsel()
    for i in M._reserved:
        self.assertRaises(cookies.CookieError, M.set, i, '%s_value' % i, '%s_value' % i)
    for i in 'thou cast _the- !holy! ^hand| +*grenade~'.split():
        M['path'] = '/foo'
        M.set(i, '%s_val' % i, '%s_coded_val' % i)
        self.assertEqual(M.key, i)
        self.assertEqual(M.value, '%s_val' % i)
        self.assertEqual(M.coded_value, '%s_coded_val' % i)
        self.assertEqual(M.output(), 'Set-Cookie: %s=%s; Path=/foo' % (i, '%s_coded_val' % i))
        expected_js_output = '\n        <script type="text/javascript">\n        <!-- begin hiding\n        document.cookie = "%s=%s; Path=/foo";\n        // end hiding -->\n        </script>\n        ' % (i, '%s_coded_val' % i)
        self.assertEqual(M.js_output(), expected_js_output)
    for i in ['foo bar', 'foo@bar']:
        self.assertRaises(cookies.CookieError, M.set, i, '%s_value' % i, '%s_value' % i)
