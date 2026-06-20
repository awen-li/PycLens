# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keyword.py
# case: Test_iskeyword_test_changing_the_softkwlist_does_not_affect_issoftkeyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldlist = keyword.softkwlist
    self.addCleanup(setattr, keyword, 'softkwlist', oldlist)
    keyword.softkwlist = ['foo', 'bar', 'spam', 'egs', 'case']
    self.assertFalse(keyword.issoftkeyword('spam'))
