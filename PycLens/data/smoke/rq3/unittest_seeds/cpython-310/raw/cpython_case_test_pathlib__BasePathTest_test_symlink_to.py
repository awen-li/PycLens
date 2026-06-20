# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_symlink_to

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    target = P / 'fileA'
    link = P / 'dirA' / 'linkAA'
    link.symlink_to(target)
    self.assertEqual(link.stat(), target.stat())
    self.assertNotEqual(link.lstat(), target.stat())
    link = P / 'dirA' / 'linkAAA'
    link.symlink_to(str(target))
    self.assertEqual(link.stat(), target.stat())
    self.assertNotEqual(link.lstat(), target.stat())
    self.assertFalse(link.is_dir())
    target = P / 'dirB'
    link = P / 'dirA' / 'linkAAAA'
    link.symlink_to(target, target_is_directory=True)
    self.assertEqual(link.stat(), target.stat())
    self.assertNotEqual(link.lstat(), target.stat())
    self.assertTrue(link.is_dir())
    self.assertTrue(list(link.iterdir()))
