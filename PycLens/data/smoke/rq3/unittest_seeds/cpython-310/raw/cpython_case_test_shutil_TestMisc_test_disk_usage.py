# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMisc_test_disk_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    usage = shutil.disk_usage(os.path.dirname(__file__))
    for attr in ('total', 'used', 'free'):
        self.assertIsInstance(getattr(usage, attr), int)
    self.assertGreater(usage.total, 0)
    self.assertGreater(usage.used, 0)
    self.assertGreaterEqual(usage.free, 0)
    self.assertGreaterEqual(usage.total, usage.used)
    self.assertGreater(usage.total, usage.free)
    shutil.disk_usage(__file__)
