# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_splice_offset_out

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN4 = os_helper.TESTFN + '.4'
    data = b'0123456789'
    bytes_to_copy = 6
    out_seek = 3
    create_file(os_helper.TESTFN, data)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    (read_fd, write_fd) = os.pipe()
    self.addCleanup(lambda : os.close(read_fd))
    self.addCleanup(lambda : os.close(write_fd))
    os.write(write_fd, data)
    out_file = open(TESTFN4, 'w+b')
    self.addCleanup(os_helper.unlink, TESTFN4)
    self.addCleanup(out_file.close)
    out_fd = out_file.fileno()
    try:
        i = os.splice(read_fd, out_fd, bytes_to_copy, offset_dst=out_seek)
    except OSError as e:
        if e.errno != errno.ENOSYS:
            raise
        self.skipTest(e)
    else:
        self.assertIn(i, range(0, bytes_to_copy + 1))
        with open(TESTFN4, 'rb') as in_file:
            read = in_file.read()
        self.assertEqual(read[:out_seek], b'\x00' * out_seek)
        self.assertEqual(read[out_seek:], data[:i])
