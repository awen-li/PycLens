# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_trailers_overflow_32bits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.server.handler_instance.accumulate = False
    with self.assertRaises(OSError) as cm:
        os.sendfile(self.sockno, self.fileno, 0, 0, trailers=[b'x' * 2 ** 16] * 2 ** 15)
    self.assertEqual(cm.exception.errno, errno.EINVAL)
