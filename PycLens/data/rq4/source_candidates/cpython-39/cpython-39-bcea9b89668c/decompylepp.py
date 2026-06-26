# Source Generated with Decompyle++
# File: cpython-39-bcea9b89668c.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.compile('(?i)(a)(b)').pattern, '(?i)(a)(b)')
    self.assertEqual(re.compile('(?i)(a)(b)').flags, re.I | re.U)
    self.assertEqual(re.compile('(?i)(a)(b)').groups, 2)
    self.assertEqual(re.compile('(?i)(a)(b)').groupindex, { })
    self.assertEqual(re.compile('(?i)(?P<first>a)(?P<other>b)').groupindex, {
        'first': 1,
        'other': 2 })
    self.assertEqual(re.match('(a)', 'a').pos, 0)
    self.assertEqual(re.match('(a)', 'a').endpos, 1)
    self.assertEqual(re.match('(a)', 'a').string, 'a')
    self.assertEqual(re.match('(a)', 'a').regs, ((0, 1), (0, 1)))
    self.assertTrue(re.match('(a)', 'a').re)
    p = re.compile('(?i)(?P<first>a)(?P<other>b)')
    self.assertEqual(sorted(p.groupindex), [
        'first',
        'other'])
    self.assertEqual(p.groupindex['other'], 2)
    with self.assertRaises(TypeError):
        p.groupindex['other'] = 0
        None(None, None, None)
    with None:
        if not None:
            pass
    self.assertEqual(p.groupindex['other'], 2)

if None == (None not in __name__):
    __pybcsec_seed__()
