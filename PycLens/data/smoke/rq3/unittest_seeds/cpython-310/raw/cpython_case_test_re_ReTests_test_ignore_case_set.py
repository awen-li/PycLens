# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_ignore_case_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.match('[19A]', 'A', re.I))
    self.assertTrue(re.match('[19a]', 'a', re.I))
    self.assertTrue(re.match('[19a]', 'A', re.I))
    self.assertTrue(re.match('[19A]', 'a', re.I))
    self.assertTrue(re.match(b'[19A]', b'A', re.I))
    self.assertTrue(re.match(b'[19a]', b'a', re.I))
    self.assertTrue(re.match(b'[19a]', b'A', re.I))
    self.assertTrue(re.match(b'[19A]', b'a', re.I))
    assert 'K'.lower() == 'K'.lower() == 'k'
    self.assertTrue(re.match('[19K]', 'K', re.I))
    self.assertTrue(re.match('[19k]', 'K', re.I))
    self.assertTrue(re.match('[19\\u212a]', 'K', re.I))
    self.assertTrue(re.match('[19\\u212a]', 'k', re.I))
    assert 's'.upper() == 'ſ'.upper() == 'S'
    self.assertTrue(re.match('[19S]', 'ſ', re.I))
    self.assertTrue(re.match('[19s]', 'ſ', re.I))
    self.assertTrue(re.match('[19\\u017f]', 'S', re.I))
    self.assertTrue(re.match('[19\\u017f]', 's', re.I))
    assert 'в'.upper() == 'ᲀ'.upper() == 'В'
    self.assertTrue(re.match('[19\\u0412]', 'в', re.I))
    self.assertTrue(re.match('[19\\u0412]', 'ᲀ', re.I))
    self.assertTrue(re.match('[19\\u0432]', 'В', re.I))
    self.assertTrue(re.match('[19\\u0432]', 'ᲀ', re.I))
    self.assertTrue(re.match('[19\\u1c80]', 'В', re.I))
    self.assertTrue(re.match('[19\\u1c80]', 'в', re.I))
    assert 'ﬅ'.upper() == 'ﬆ'.upper() == 'ST'
    self.assertTrue(re.match('[19\\ufb05]', 'ﬆ', re.I))
    self.assertTrue(re.match('[19\\ufb06]', 'ﬅ', re.I))
