# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_string_boundaries

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.search('\\b(abc)\\b', 'abc').group(1), 'abc')
    self.assertTrue(re.match('\\b', 'abc'))
    self.assertTrue(re.search('\\B', 'abc'))
    self.assertFalse(re.match('\\B', 'abc'))
    self.assertIsNone(re.search('\\B', ''))
    self.assertIsNone(re.search('\\b', ''))
    self.assertEqual(len(re.findall('\\b', 'a')), 2)
    self.assertEqual(len(re.findall('\\B', 'a')), 0)
    self.assertEqual(len(re.findall('\\b', ' ')), 0)
    self.assertEqual(len(re.findall('\\b', '   ')), 0)
    self.assertEqual(len(re.findall('\\B', ' ')), 2)
