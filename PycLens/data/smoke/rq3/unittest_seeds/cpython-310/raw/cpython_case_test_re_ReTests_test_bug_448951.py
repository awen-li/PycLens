# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_448951

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for op in ('', '?', '*'):
        self.assertEqual(re.match('((.%s):)?z' % op, 'z').groups(), (None, None))
        self.assertEqual(re.match('((.%s):)?z' % op, 'a:z').groups(), ('a:', 'a'))
