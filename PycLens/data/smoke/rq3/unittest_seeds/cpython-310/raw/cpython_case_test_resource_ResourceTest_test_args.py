# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, resource.getrlimit)
    self.assertRaises(TypeError, resource.getrlimit, 42, 42)
    self.assertRaises(TypeError, resource.setrlimit)
    self.assertRaises(TypeError, resource.setrlimit, 42, 42, 42)
