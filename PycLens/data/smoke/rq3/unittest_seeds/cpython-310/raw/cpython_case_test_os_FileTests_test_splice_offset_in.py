# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_splice_offset_in

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN4 = os_helper.TESTFN + '.4'
    data = b'0123456789'
    bytes_to_copy = 6
    in_skip = 3
    create_file(os_helper.TESTFN, data)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    in_file = open(os_helper.TESTFN, 'rb')
    self.addCleanup(in_file.close)
    in_fd = in_file.fileno()
    (read_fd, write_fd) = os.pipe()
    self.addCleanup(lambda : os.close(read_fd))
    self.addCleanup(lambda : os.close(write_fd))
    try:
        i = os.splice(in_fd, write_fd, bytes_to_copy, offset_src=in_skip)
    except OSError as e:
        if e.errno != errno.ENOSYS:
            raise
        self.skipTest(e)
    else:
        self.assertIn(i, range(0, bytes_to_copy + 1))
        read = os.read(read_fd, 100)
        self.assertEqual(read, data[in_skip:in_skip + i])
