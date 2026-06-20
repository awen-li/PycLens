# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: PEP626Tests_test_lineno_after_other_except

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def other_except():
        try:
            1 / 0
        except TypeError as ex:
            pass
    self.lineno_after_raise(other_except, 3)
