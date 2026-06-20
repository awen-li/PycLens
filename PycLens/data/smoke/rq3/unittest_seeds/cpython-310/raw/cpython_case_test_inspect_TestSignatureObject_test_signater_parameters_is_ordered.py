# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signater_parameters_is_ordered

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p1 = inspect.signature(lambda x, y: None).parameters
    p2 = inspect.signature(lambda y, x: None).parameters
    self.assertNotEqual(p1, p2)
