# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_method_descriptor_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(str.join, types.MethodDescriptorType)
    self.assertIsInstance(list.append, types.MethodDescriptorType)
    self.assertIsInstance(''.join, types.BuiltinMethodType)
    self.assertIsInstance([].append, types.BuiltinMethodType)
    self.assertIsInstance(int.__dict__['from_bytes'], types.ClassMethodDescriptorType)
    self.assertIsInstance(int.from_bytes, types.BuiltinMethodType)
    self.assertIsInstance(int.__new__, types.BuiltinMethodType)
