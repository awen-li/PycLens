# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestMatchAbbrev_test_match_abbrev_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '--f'
    wordmap = {'--foz': None, '--foo': None, '--fie': None}
    self.assertRaises(_match_abbrev, (s, wordmap), None, BadOptionError, 'ambiguous option: --f (--fie, --foo, --foz?)')
