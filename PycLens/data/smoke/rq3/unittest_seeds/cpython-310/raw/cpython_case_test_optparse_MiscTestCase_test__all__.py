# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: MiscTestCase_test__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_exported = {'check_builtin', 'AmbiguousOptionError', 'NO_DEFAULT'}
    support.check__all__(self, optparse, not_exported=not_exported)
