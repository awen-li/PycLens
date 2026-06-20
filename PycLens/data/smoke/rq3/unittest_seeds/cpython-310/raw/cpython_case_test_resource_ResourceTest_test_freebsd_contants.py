# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_freebsd_contants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for attr in ['SWAP', 'SBSIZE', 'NPTS']:
        with contextlib.suppress(AttributeError):
            self.assertIsInstance(getattr(resource, 'RLIMIT_' + attr), int)
