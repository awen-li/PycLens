# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestConflictingDefaults_test_conflict_default_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-q', action='store_false', dest='verbose', default=None)
    self.assertParseOK([], {'verbose': None}, [])
