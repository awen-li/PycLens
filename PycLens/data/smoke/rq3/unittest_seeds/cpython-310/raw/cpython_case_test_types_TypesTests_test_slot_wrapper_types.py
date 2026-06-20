# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_slot_wrapper_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(object.__init__, types.WrapperDescriptorType)
    self.assertIsInstance(object.__str__, types.WrapperDescriptorType)
    self.assertIsInstance(object.__lt__, types.WrapperDescriptorType)
    self.assertIsInstance(int.__lt__, types.WrapperDescriptorType)
