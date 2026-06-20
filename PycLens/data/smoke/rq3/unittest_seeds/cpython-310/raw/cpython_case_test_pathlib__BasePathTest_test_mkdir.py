# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    p = P / 'newdirA'
    self.assertFalse(p.exists())
    p.mkdir()
    self.assertTrue(p.exists())
    self.assertTrue(p.is_dir())
    with self.assertRaises(OSError) as cm:
        p.mkdir()
    self.assertEqual(cm.exception.errno, errno.EEXIST)
