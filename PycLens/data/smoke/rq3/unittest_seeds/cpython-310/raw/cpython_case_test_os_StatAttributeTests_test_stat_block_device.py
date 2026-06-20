# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_stat_block_device

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = '//./' + os.path.splitdrive(os.getcwd())[0]
    result = os.stat(fname)
    self.assertEqual(result.st_mode, stat.S_IFBLK)
