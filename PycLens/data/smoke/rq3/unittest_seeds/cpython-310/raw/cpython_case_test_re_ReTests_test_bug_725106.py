# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_725106

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('^((a)|b)*', 'abc').groups(), ('b', 'a'))
    self.assertEqual(re.match('^(([ab])|c)*', 'abc').groups(), ('c', 'b'))
    self.assertEqual(re.match('^((d)|[ab])*', 'abc').groups(), ('b', None))
    self.assertEqual(re.match('^((a)c|[ab])*', 'abc').groups(), ('b', None))
    self.assertEqual(re.match('^((a)|b)*?c', 'abc').groups(), ('b', 'a'))
    self.assertEqual(re.match('^(([ab])|c)*?d', 'abcd').groups(), ('c', 'b'))
    self.assertEqual(re.match('^((d)|[ab])*?c', 'abc').groups(), ('b', None))
    self.assertEqual(re.match('^((a)c|[ab])*?c', 'abc').groups(), ('b', None))
