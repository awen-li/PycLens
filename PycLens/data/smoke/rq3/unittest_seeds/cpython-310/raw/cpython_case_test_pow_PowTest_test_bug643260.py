# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pow.py
# case: PowTest_test_bug643260

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestRpow:

        def __rpow__(self, other):
            return None
    None ** TestRpow()
