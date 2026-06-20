# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: PEP626Tests_test_lineno_after_raise_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def simple():
        1 / 0
        pass
    self.lineno_after_raise(simple, 1)
