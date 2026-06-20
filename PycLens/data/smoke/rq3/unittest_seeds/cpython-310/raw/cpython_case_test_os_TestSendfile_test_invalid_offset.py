# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_invalid_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(OSError) as cm:
        os.sendfile(self.sockno, self.fileno, -1, 4096)
    self.assertEqual(cm.exception.errno, errno.EINVAL)
