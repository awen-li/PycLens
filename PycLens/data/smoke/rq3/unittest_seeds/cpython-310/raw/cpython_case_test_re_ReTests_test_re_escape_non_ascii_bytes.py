# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_escape_non_ascii_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = 'y☠y☠y'.encode('utf-8')
    b_escaped = re.escape(b)
    self.assertEqual(b_escaped, b)
    self.assertMatch(b_escaped, b)
    res = re.findall(re.escape('☠'.encode('utf-8')), b)
    self.assertEqual(len(res), 2)
