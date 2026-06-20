# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_pagesize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pagesize = resource.getpagesize()
    self.assertIsInstance(pagesize, int)
    self.assertGreaterEqual(pagesize, 0)
