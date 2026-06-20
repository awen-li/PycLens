# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir_no_parents_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE, 'fileA')
    self.assertTrue(p.exists())
    with self.assertRaises(FileExistsError) as cm:
        p.mkdir()
    self.assertEqual(cm.exception.errno, errno.EEXIST)
    with self.assertRaises(FileExistsError) as cm:
        p.mkdir(exist_ok=True)
    self.assertEqual(cm.exception.errno, errno.EEXIST)
