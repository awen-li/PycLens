# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_34294

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'a\tx'
    p = '\\b(?=(\\t)|(x))x'
    self.assertEqual(re.search(p, s).groups(), (None, 'x'))
    s = 'ab'
    p = '(?=(.)(.)?)'
    self.assertEqual(re.findall(p, s), [('a', 'b'), ('b', '')])
    self.assertEqual([m.groups() for m in re.finditer(p, s)], [('a', 'b'), ('b', None)])
    p = '(?=<(?P<tag>\\w+)/?>(?:(?P<text>.+?)</(?P=tag)>)?)'
    s = '<test><foo2/></test>'
    self.assertEqual(re.findall(p, s), [('test', '<foo2/>'), ('foo2', '')])
    self.assertEqual([m.groupdict() for m in re.finditer(p, s)], [{'tag': 'test', 'text': '<foo2/>'}, {'tag': 'foo2', 'text': None}])
    s = '<test>Hello</test><foo/>'
    self.assertEqual([m.groupdict() for m in re.finditer(p, s)], [{'tag': 'test', 'text': 'Hello'}, {'tag': 'foo', 'text': None}])
    s = '<test>Hello</test><foo/><foo/>'
    self.assertEqual([m.groupdict() for m in re.finditer(p, s)], [{'tag': 'test', 'text': 'Hello'}, {'tag': 'foo', 'text': None}, {'tag': 'foo', 'text': None}])
