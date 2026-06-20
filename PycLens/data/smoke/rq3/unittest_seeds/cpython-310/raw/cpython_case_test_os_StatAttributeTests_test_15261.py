# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_15261

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    try:
        os.stat(r)
    finally:
        os.close(r)
        os.close(w)
    with self.assertRaises(OSError) as ctx:
        os.stat(r)
    self.assertEqual(ctx.exception.errno, errno.EBADF)
