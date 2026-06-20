# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keyword.py
# case: Test_iskeyword_test_changing_the_kwlist_does_not_affect_iskeyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldlist = keyword.kwlist
    self.addCleanup(setattr, keyword, 'kwlist', oldlist)
    keyword.kwlist = ['its', 'all', 'eggs', 'beans', 'and', 'a', 'slice']
    self.assertFalse(keyword.iskeyword('eggs'))
