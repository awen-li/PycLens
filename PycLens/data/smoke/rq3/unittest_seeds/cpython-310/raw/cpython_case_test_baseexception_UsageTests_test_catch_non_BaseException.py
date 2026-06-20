# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_baseexception.py
# case: UsageTests_test_catch_non_BaseException

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NonBaseException(object):
        pass
    self.catch_fails(NonBaseException)
    self.catch_fails(NonBaseException())
