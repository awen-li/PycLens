# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (orig, expect) in parse_strict_test_cases:
        d = do_test(orig, 'GET')
        self.assertEqual(d, expect, 'Error parsing %s method GET' % repr(orig))
        d = do_test(orig, 'POST')
        self.assertEqual(d, expect, 'Error parsing %s method POST' % repr(orig))
        env = {'QUERY_STRING': orig}
        fs = cgi.FieldStorage(environ=env)
        if isinstance(expect, dict):
            self.assertEqual(len(expect), len(fs))
            self.assertCountEqual(expect.keys(), fs.keys())
            self.assertEqual(fs.getvalue('nonexistent field', 'default'), 'default')
            for key in expect.keys():
                expect_val = expect[key]
                self.assertIn(key, fs)
                if len(expect_val) > 1:
                    self.assertEqual(fs.getvalue(key), expect_val)
                else:
                    self.assertEqual(fs.getvalue(key), expect_val[0])
