# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_mkfifo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform == 'vxworks':
        fifo_path = os.path.join('/fifos/', os_helper.TESTFN)
    else:
        fifo_path = os_helper.TESTFN
    os_helper.unlink(fifo_path)
    self.addCleanup(os_helper.unlink, fifo_path)
    try:
        posix.mkfifo(fifo_path, stat.S_IRUSR | stat.S_IWUSR)
    except PermissionError as e:
        self.skipTest('posix.mkfifo(): %s' % e)
    self.assertTrue(stat.S_ISFIFO(posix.stat(fifo_path).st_mode))
