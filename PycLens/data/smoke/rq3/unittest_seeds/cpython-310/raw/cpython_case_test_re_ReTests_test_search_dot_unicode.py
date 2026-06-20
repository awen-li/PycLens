# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_search_dot_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.search('123.*-', '123abc-'))
    self.assertTrue(re.search('123.*-', '123é-'))
    self.assertTrue(re.search('123.*-', '123€-'))
    self.assertTrue(re.search('123.*-', '123\U0010ffff-'))
    self.assertTrue(re.search('123.*-', '123é€\U0010ffff-'))
