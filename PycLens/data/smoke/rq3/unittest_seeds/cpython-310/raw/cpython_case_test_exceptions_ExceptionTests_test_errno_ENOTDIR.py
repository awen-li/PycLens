# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_errno_ENOTDIR

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(OSError) as cm:
        os.listdir(__file__)
    self.assertEqual(cm.exception.errno, errno.ENOTDIR, cm.exception)
