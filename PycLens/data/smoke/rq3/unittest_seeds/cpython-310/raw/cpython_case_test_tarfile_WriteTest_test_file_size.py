# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_file_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tmpname, self.mode)
    try:
        path = os.path.join(TEMPDIR, 'file')
        with open(path, 'wb'):
            pass
        tarinfo = tar.gettarinfo(path)
        self.assertEqual(tarinfo.size, 0)
        with open(path, 'wb') as fobj:
            fobj.write(b'aaa')
        tarinfo = tar.gettarinfo(path)
        self.assertEqual(tarinfo.size, 3)
    finally:
        tar.close()
