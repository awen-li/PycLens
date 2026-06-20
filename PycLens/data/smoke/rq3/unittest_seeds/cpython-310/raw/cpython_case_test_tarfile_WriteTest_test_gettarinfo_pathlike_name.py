# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_gettarinfo_pathlike_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tmpname, self.mode) as tar:
        path = pathlib.Path(TEMPDIR) / 'file'
        with open(path, 'wb') as fobj:
            fobj.write(b'aaa')
        tarinfo = tar.gettarinfo(path)
        tarinfo2 = tar.gettarinfo(os.fspath(path))
        self.assertIsInstance(tarinfo.name, str)
        self.assertEqual(tarinfo.name, tarinfo2.name)
        self.assertEqual(tarinfo.size, 3)
