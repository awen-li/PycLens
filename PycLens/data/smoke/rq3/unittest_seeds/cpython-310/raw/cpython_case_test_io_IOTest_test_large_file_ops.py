# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_large_file_ops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform[:3] == 'win' or sys.platform == 'darwin':
        support.requires('largefile', 'test requires %s bytes and a long time to run' % self.LARGE)
    with self.open(os_helper.TESTFN, 'w+b', 0) as f:
        self.large_file_ops(f)
    with self.open(os_helper.TESTFN, 'w+b') as f:
        self.large_file_ops(f)
