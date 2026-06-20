# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_copy_file_range_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN4 = os_helper.TESTFN + '.4'
    data = b'0123456789'
    bytes_to_copy = 6
    in_skip = 3
    out_seek = 5
    create_file(os_helper.TESTFN, data)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    in_file = open(os_helper.TESTFN, 'rb')
    self.addCleanup(in_file.close)
    in_fd = in_file.fileno()
    out_file = open(TESTFN4, 'w+b')
    self.addCleanup(os_helper.unlink, TESTFN4)
    self.addCleanup(out_file.close)
    out_fd = out_file.fileno()
    try:
        i = os.copy_file_range(in_fd, out_fd, bytes_to_copy, offset_src=in_skip, offset_dst=out_seek)
    except OSError as e:
        if e.errno != errno.ENOSYS:
            raise
        self.skipTest(e)
    else:
        self.assertIn(i, range(0, bytes_to_copy + 1))
        with open(TESTFN4, 'rb') as in_file:
            read = in_file.read()
        self.assertEqual(read[:out_seek], b'\x00' * out_seek)
        self.assertEqual(read[out_seek:], data[in_skip:in_skip + i])
