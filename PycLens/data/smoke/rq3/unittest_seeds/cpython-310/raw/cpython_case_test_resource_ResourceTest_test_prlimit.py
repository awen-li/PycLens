# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_prlimit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, resource.prlimit)
    self.assertRaises(ProcessLookupError, resource.prlimit, -1, resource.RLIMIT_AS)
    limit = resource.getrlimit(resource.RLIMIT_AS)
    self.assertEqual(resource.prlimit(0, resource.RLIMIT_AS), limit)
    self.assertEqual(resource.prlimit(0, resource.RLIMIT_AS, limit), limit)
