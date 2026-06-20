# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_samefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileA_path = os.path.join(BASE, 'fileA')
    fileB_path = os.path.join(BASE, 'dirB', 'fileB')
    p = self.cls(fileA_path)
    pp = self.cls(fileA_path)
    q = self.cls(fileB_path)
    self.assertTrue(p.samefile(fileA_path))
    self.assertTrue(p.samefile(pp))
    self.assertFalse(p.samefile(fileB_path))
    self.assertFalse(p.samefile(q))
    non_existent = os.path.join(BASE, 'foo')
    r = self.cls(non_existent)
    self.assertRaises(FileNotFoundError, p.samefile, r)
    self.assertRaises(FileNotFoundError, p.samefile, non_existent)
    self.assertRaises(FileNotFoundError, r.samefile, p)
    self.assertRaises(FileNotFoundError, r.samefile, non_existent)
    self.assertRaises(FileNotFoundError, r.samefile, r)
    self.assertRaises(FileNotFoundError, r.samefile, non_existent)
