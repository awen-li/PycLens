# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_prlimit_refcount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadSeq:

        def __len__(self):
            return 2

        def __getitem__(self, key):
            return limits[key] - 1
    limits = resource.getrlimit(resource.RLIMIT_AS)
    self.assertEqual(resource.prlimit(0, resource.RLIMIT_AS, BadSeq()), limits)
