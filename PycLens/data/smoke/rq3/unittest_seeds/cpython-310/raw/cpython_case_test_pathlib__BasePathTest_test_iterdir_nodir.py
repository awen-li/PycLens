# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_iterdir_nodir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE, 'fileA')
    with self.assertRaises(OSError) as cm:
        next(p.iterdir())
    self.assertIn(cm.exception.errno, (errno.ENOTDIR, errno.ENOENT, errno.EINVAL))
