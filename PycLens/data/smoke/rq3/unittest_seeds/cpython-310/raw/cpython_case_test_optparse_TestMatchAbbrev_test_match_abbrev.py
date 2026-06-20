# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestMatchAbbrev_test_match_abbrev

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(_match_abbrev('--f', {'--foz': None, '--foo': None, '--fie': None, '--f': None}), '--f')
