# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_zerowidth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.split('\\b', 'a::bc'), ['', 'a', '::', 'bc', ''])
    self.assertEqual(re.split('\\b|:+', 'a::bc'), ['', 'a', '', '', 'bc', ''])
    self.assertEqual(re.split('(?<!\\w)(?=\\w)|:+', 'a::bc'), ['', 'a', '', 'bc'])
    self.assertEqual(re.split('(?<=\\w)(?!\\w)|:+', 'a::bc'), ['a', '', 'bc', ''])
    self.assertEqual(re.sub('\\b', '-', 'a::bc'), '-a-::-bc-')
    self.assertEqual(re.sub('\\b|:+', '-', 'a::bc'), '-a---bc-')
    self.assertEqual(re.sub('(\\b|:+)', '[\\1]', 'a::bc'), '[]a[][::][]bc[]')
    self.assertEqual(re.findall('\\b|:+', 'a::bc'), ['', '', '::', '', ''])
    self.assertEqual(re.findall('\\b|\\w+', 'a::bc'), ['', 'a', '', '', 'bc', ''])
    self.assertEqual([m.span() for m in re.finditer('\\b|:+', 'a::bc')], [(0, 0), (1, 1), (1, 3), (3, 3), (5, 5)])
    self.assertEqual([m.span() for m in re.finditer('\\b|\\w+', 'a::bc')], [(0, 0), (0, 1), (1, 1), (3, 3), (3, 5), (5, 5)])
