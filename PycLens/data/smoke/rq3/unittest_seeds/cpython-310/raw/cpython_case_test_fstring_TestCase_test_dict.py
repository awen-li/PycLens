# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'"': 'dquote', "'": 'squote', 'foo': 'bar'}
    self.assertEqual(f"""{d["'"]}""", 'squote')
    self.assertEqual(f"""{d['"']}""", 'dquote')
    self.assertEqual(f"{d['foo']}", 'bar')
    self.assertEqual(f"{d['foo']}", 'bar')
