# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.compile('(?i)(a)(b)').pattern, '(?i)(a)(b)')
    self.assertEqual(re.compile('(?i)(a)(b)').flags, re.I | re.U)
    self.assertEqual(re.compile('(?i)(a)(b)').groups, 2)
    self.assertEqual(re.compile('(?i)(a)(b)').groupindex, {})
    self.assertEqual(re.compile('(?i)(?P<first>a)(?P<other>b)').groupindex, {'first': 1, 'other': 2})
    self.assertEqual(re.match('(a)', 'a').pos, 0)
    self.assertEqual(re.match('(a)', 'a').endpos, 1)
    self.assertEqual(re.match('(a)', 'a').string, 'a')
    self.assertEqual(re.match('(a)', 'a').regs, ((0, 1), (0, 1)))
    self.assertTrue(re.match('(a)', 'a').re)
    p = re.compile('(?i)(?P<first>a)(?P<other>b)')
    self.assertEqual(sorted(p.groupindex), ['first', 'other'])
    self.assertEqual(p.groupindex['other'], 2)
    with self.assertRaises(TypeError):
        p.groupindex['other'] = 0
    self.assertEqual(p.groupindex['other'], 2)
