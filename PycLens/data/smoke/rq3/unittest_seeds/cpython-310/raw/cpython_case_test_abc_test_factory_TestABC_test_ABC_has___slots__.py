# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_ABC_has___slots__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(abc.ABC, '__slots__'))
