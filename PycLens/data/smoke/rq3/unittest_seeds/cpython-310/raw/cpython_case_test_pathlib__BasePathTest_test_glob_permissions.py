# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_glob_permissions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    base = P(BASE) / 'permissions'
    base.mkdir()
    file1 = base / 'file1'
    file1.touch()
    file2 = base / 'file2'
    file2.touch()
    subdir = base / 'subdir'
    file3 = base / 'file3'
    file3.symlink_to(subdir / 'other')
    with mock.patch('os.scandir') as scandir:
        scandir.return_value = sorted(os.scandir(base))
        self.assertEqual(len(set(base.glob('*'))), 3)
    subdir.mkdir()
    with mock.patch('os.scandir') as scandir:
        scandir.return_value = sorted(os.scandir(base))
        self.assertEqual(len(set(base.glob('*'))), 4)
    subdir.chmod(0)
    with mock.patch('os.scandir') as scandir:
        scandir.return_value = sorted(os.scandir(base))
        self.assertEqual(len(set(base.glob('*'))), 4)
