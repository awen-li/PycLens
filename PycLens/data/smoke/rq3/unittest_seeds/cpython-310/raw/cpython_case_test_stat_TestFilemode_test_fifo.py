# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_fifo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform == 'vxworks':
        fifo_path = os.path.join('/fifos/', TESTFN)
    else:
        fifo_path = TESTFN
    self.addCleanup(os_helper.unlink, fifo_path)
    try:
        os.mkfifo(fifo_path, 448)
    except PermissionError as e:
        self.skipTest('os.mkfifo(): %s' % e)
    (st_mode, modestr) = self.get_mode(fifo_path)
    self.assertEqual(modestr, 'prwx------')
    self.assertS_IS('FIFO', st_mode)
