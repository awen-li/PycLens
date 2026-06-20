# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_method_wrapper_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(object().__init__, types.MethodWrapperType)
    self.assertIsInstance(object().__str__, types.MethodWrapperType)
    self.assertIsInstance(object().__lt__, types.MethodWrapperType)
    self.assertIsInstance(42 .__lt__, types.MethodWrapperType)
