# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_getrusage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, resource.getrusage)
    self.assertRaises(TypeError, resource.getrusage, 42, 42)
    usageself = resource.getrusage(resource.RUSAGE_SELF)
    usagechildren = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        usageboth = resource.getrusage(resource.RUSAGE_BOTH)
    except (ValueError, AttributeError):
        pass
    try:
        usage_thread = resource.getrusage(resource.RUSAGE_THREAD)
    except (ValueError, AttributeError):
        pass
