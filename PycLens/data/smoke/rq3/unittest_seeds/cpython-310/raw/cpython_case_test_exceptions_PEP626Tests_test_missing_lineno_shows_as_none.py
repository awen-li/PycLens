# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: PEP626Tests_test_missing_lineno_shows_as_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        1 / 0
    self.lineno_after_raise(f, 1)
    f.__code__ = f.__code__.replace(co_linetable=b'\x04\x80\xff\x80')
    self.lineno_after_raise(f, None)
