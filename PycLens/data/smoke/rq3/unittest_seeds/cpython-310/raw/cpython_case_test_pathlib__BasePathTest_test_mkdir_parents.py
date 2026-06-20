# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE, 'newdirB', 'newdirC')
    self.assertFalse(p.exists())
    with self.assertRaises(OSError) as cm:
        p.mkdir()
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    p.mkdir(parents=True)
    self.assertTrue(p.exists())
    self.assertTrue(p.is_dir())
    with self.assertRaises(OSError) as cm:
        p.mkdir(parents=True)
    self.assertEqual(cm.exception.errno, errno.EEXIST)
    mode = stat.S_IMODE(p.stat().st_mode)
    p = self.cls(BASE, 'newdirD', 'newdirE')
    p.mkdir(365, parents=True)
    self.assertTrue(p.exists())
    self.assertTrue(p.is_dir())
    if os.name != 'nt':
        self.assertEqual(stat.S_IMODE(p.stat().st_mode), 3949 & mode)
    self.assertEqual(stat.S_IMODE(p.parent.stat().st_mode), mode)
