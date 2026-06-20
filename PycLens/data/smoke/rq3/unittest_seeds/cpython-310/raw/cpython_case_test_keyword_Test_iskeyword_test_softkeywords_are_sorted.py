# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keyword.py
# case: Test_iskeyword_test_softkeywords_are_sorted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertListEqual(sorted(keyword.softkwlist), keyword.softkwlist)
