# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_no_single_dash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("invalid long option string '-debug': must start with --, followed by non-dash", ['-debug'])
    self.assertOptionError("option -d: invalid long option string '-debug': must start with --, followed by non-dash", ['-d', '-debug'])
    self.assertOptionError("invalid long option string '-debug': must start with --, followed by non-dash", ['-debug', '--debug'])
