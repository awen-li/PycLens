# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_hardlink_to

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    target = P / 'fileA'
    size = target.stat().st_size
    link = P / 'dirA' / 'fileAA'
    link.hardlink_to(target)
    self.assertEqual(link.stat().st_size, size)
    self.assertTrue(os.path.samefile(target, link))
    self.assertTrue(target.exists())
    link2 = P / 'dirA' / 'fileAAA'
    target2 = rel_join('fileA')
    link2.hardlink_to(target2)
    self.assertEqual(os.stat(target2).st_size, size)
    self.assertTrue(link2.exists())
