# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_separator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parse_semicolon = [('x=1;y=2.0', {'x': ['1'], 'y': ['2.0']}), ('x=1;y=2.0;z=2-3.%2b0', {'x': ['1'], 'y': ['2.0'], 'z': ['2-3.+0']}), (';', ValueError("bad query field: ''")), (';;', ValueError("bad query field: ''")), ('=;a', ValueError("bad query field: 'a'")), (';b=a', ValueError("bad query field: ''")), ('b;=a', ValueError("bad query field: 'b'")), ('a=a+b;b=b+c', {'a': ['a b'], 'b': ['b c']}), ('a=a+b;a=b+a', {'a': ['a b', 'b a']})]
    for (orig, expect) in parse_semicolon:
        env = {'QUERY_STRING': orig}
        fs = cgi.FieldStorage(separator=';', environ=env)
        if isinstance(expect, dict):
            for key in expect.keys():
                expect_val = expect[key]
                self.assertIn(key, fs)
                if len(expect_val) > 1:
                    self.assertEqual(fs.getvalue(key), expect_val)
                else:
                    self.assertEqual(fs.getvalue(key), expect_val[0])
