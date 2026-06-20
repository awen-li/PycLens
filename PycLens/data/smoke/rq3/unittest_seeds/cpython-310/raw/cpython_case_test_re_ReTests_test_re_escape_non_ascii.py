# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_escape_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'xxx☠☠☠xxx'
    s_escaped = re.escape(s)
    self.assertEqual(s_escaped, s)
    self.assertMatch(s_escaped, s)
    self.assertMatch('.%s+.' % re.escape('☠'), s, 'x☠☠☠x', (2, 7), re.search)
