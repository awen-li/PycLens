# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_pathlike_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarname = pathlib.Path(self.tarname)
    with tarfile.open(tarname, mode=self.mode) as tar:
        self.assertIsInstance(tar.name, str)
        self.assertEqual(tar.name, os.path.abspath(os.fspath(tarname)))
    with self.taropen(tarname) as tar:
        self.assertIsInstance(tar.name, str)
        self.assertEqual(tar.name, os.path.abspath(os.fspath(tarname)))
    with tarfile.TarFile.open(tarname, mode=self.mode) as tar:
        self.assertIsInstance(tar.name, str)
        self.assertEqual(tar.name, os.path.abspath(os.fspath(tarname)))
    if self.suffix == '':
        with tarfile.TarFile(tarname, mode='r') as tar:
            self.assertIsInstance(tar.name, str)
            self.assertEqual(tar.name, os.path.abspath(os.fspath(tarname)))
