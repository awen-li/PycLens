# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir_exist_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE, 'dirB')
    st_ctime_first = p.stat().st_ctime
    self.assertTrue(p.exists())
    self.assertTrue(p.is_dir())
    with self.assertRaises(FileExistsError) as cm:
        p.mkdir()
    self.assertEqual(cm.exception.errno, errno.EEXIST)
    p.mkdir(exist_ok=True)
    self.assertTrue(p.exists())
    self.assertEqual(p.stat().st_ctime, st_ctime_first)
