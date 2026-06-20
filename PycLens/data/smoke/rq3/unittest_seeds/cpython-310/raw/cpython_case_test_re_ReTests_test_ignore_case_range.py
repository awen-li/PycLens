# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_ignore_case_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.match('[9-a]', '_', re.I))
    self.assertIsNone(re.match('[9-A]', '_', re.I))
    self.assertTrue(re.match(b'[9-a]', b'_', re.I))
    self.assertIsNone(re.match(b'[9-A]', b'_', re.I))
    self.assertTrue(re.match('[\\xc0-\\xde]', '×', re.I))
    self.assertIsNone(re.match('[\\xc0-\\xde]', '÷', re.I))
    self.assertTrue(re.match('[\\xe0-\\xfe]', '÷', re.I))
    self.assertIsNone(re.match('[\\xe0-\\xfe]', '×', re.I))
    self.assertTrue(re.match('[\\u0430-\\u045f]', 'ѐ', re.I))
    self.assertTrue(re.match('[\\u0430-\\u045f]', 'Ѐ', re.I))
    self.assertTrue(re.match('[\\u0400-\\u042f]', 'ѐ', re.I))
    self.assertTrue(re.match('[\\u0400-\\u042f]', 'Ѐ', re.I))
    self.assertTrue(re.match('[\\U00010428-\\U0001044f]', '𐐨', re.I))
    self.assertTrue(re.match('[\\U00010428-\\U0001044f]', '𐐀', re.I))
    self.assertTrue(re.match('[\\U00010400-\\U00010427]', '𐐨', re.I))
    self.assertTrue(re.match('[\\U00010400-\\U00010427]', '𐐀', re.I))
    assert 'K'.lower() == 'K'.lower() == 'k'
    self.assertTrue(re.match('[J-M]', 'K', re.I))
    self.assertTrue(re.match('[j-m]', 'K', re.I))
    self.assertTrue(re.match('[\\u2129-\\u212b]', 'K', re.I))
    self.assertTrue(re.match('[\\u2129-\\u212b]', 'k', re.I))
    assert 's'.upper() == 'ſ'.upper() == 'S'
    self.assertTrue(re.match('[R-T]', 'ſ', re.I))
    self.assertTrue(re.match('[r-t]', 'ſ', re.I))
    self.assertTrue(re.match('[\\u017e-\\u0180]', 'S', re.I))
    self.assertTrue(re.match('[\\u017e-\\u0180]', 's', re.I))
    assert 'в'.upper() == 'ᲀ'.upper() == 'В'
    self.assertTrue(re.match('[\\u0411-\\u0413]', 'в', re.I))
    self.assertTrue(re.match('[\\u0411-\\u0413]', 'ᲀ', re.I))
    self.assertTrue(re.match('[\\u0431-\\u0433]', 'В', re.I))
    self.assertTrue(re.match('[\\u0431-\\u0433]', 'ᲀ', re.I))
    self.assertTrue(re.match('[\\u1c80-\\u1c82]', 'В', re.I))
    self.assertTrue(re.match('[\\u1c80-\\u1c82]', 'в', re.I))
    assert 'ﬅ'.upper() == 'ﬆ'.upper() == 'ST'
    self.assertTrue(re.match('[\\ufb04-\\ufb05]', 'ﬆ', re.I))
    self.assertTrue(re.match('[\\ufb06-\\ufb07]', 'ﬅ', re.I))
