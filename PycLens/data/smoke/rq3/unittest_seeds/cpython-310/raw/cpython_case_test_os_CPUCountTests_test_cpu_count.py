# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: CPUCountTests_test_cpu_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cpus = os.cpu_count()
    if cpus is not None:
        self.assertIsInstance(cpus, int)
        self.assertGreater(cpus, 0)
    else:
        self.skipTest('Could not determine the number of CPUs')
