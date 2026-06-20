# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_unbounded_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zero = '/dev/zero'
    if not os.path.exists(zero):
        self.skipTest('{0} does not exist'.format(zero))
    if sys.maxsize > 2147483647:
        self.skipTest('test can only run in a 32-bit address space')
    if support.real_max_memuse < support._2G:
        self.skipTest('test requires at least 2 GiB of memory')
    with self.open(zero, 'rb', buffering=0) as f:
        self.assertRaises(OverflowError, f.read)
    with self.open(zero, 'rb') as f:
        self.assertRaises(OverflowError, f.read)
    with self.open(zero, 'r') as f:
        self.assertRaises(OverflowError, f.read)
