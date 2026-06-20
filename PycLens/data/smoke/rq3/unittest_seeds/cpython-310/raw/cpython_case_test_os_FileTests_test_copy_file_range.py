# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_copy_file_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN2 = os_helper.TESTFN + '.3'
    data = b'0123456789'
    create_file(os_helper.TESTFN, data)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    in_file = open(os_helper.TESTFN, 'rb')
    self.addCleanup(in_file.close)
    in_fd = in_file.fileno()
    out_file = open(TESTFN2, 'w+b')
    self.addCleanup(os_helper.unlink, TESTFN2)
    self.addCleanup(out_file.close)
    out_fd = out_file.fileno()
    try:
        i = os.copy_file_range(in_fd, out_fd, 5)
    except OSError as e:
        if e.errno != errno.ENOSYS:
            raise
        self.skipTest(e)
    else:
        self.assertIn(i, range(0, 6))
        with open(TESTFN2, 'rb') as in_file:
            self.assertEqual(in_file.read(), data[:i])
