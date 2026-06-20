# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_utime_invalid_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        os.utime(self.fname, (5, 5), ns=(5, 5))
    with self.assertRaises(TypeError):
        os.utime(self.fname, [5, 5])
    with self.assertRaises(TypeError):
        os.utime(self.fname, (5,))
    with self.assertRaises(TypeError):
        os.utime(self.fname, (5, 5, 5))
    with self.assertRaises(TypeError):
        os.utime(self.fname, ns=[5, 5])
    with self.assertRaises(TypeError):
        os.utime(self.fname, ns=(5,))
    with self.assertRaises(TypeError):
        os.utime(self.fname, ns=(5, 5, 5))
    if os.utime not in os.supports_follow_symlinks:
        with self.assertRaises(NotImplementedError):
            os.utime(self.fname, (5, 5), follow_symlinks=False)
    if os.utime not in os.supports_fd:
        with open(self.fname, 'wb', 0) as fp:
            with self.assertRaises(TypeError):
                os.utime(fp.fileno(), (5, 5))
    if os.utime not in os.supports_dir_fd:
        with self.assertRaises(NotImplementedError):
            os.utime(self.fname, (5, 5), dir_fd=0)
