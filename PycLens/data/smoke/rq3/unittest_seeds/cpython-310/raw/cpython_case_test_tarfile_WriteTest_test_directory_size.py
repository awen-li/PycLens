# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_directory_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join(TEMPDIR, 'directory')
    os.mkdir(path)
    try:
        tar = tarfile.open(tmpname, self.mode)
        try:
            tarinfo = tar.gettarinfo(path)
            self.assertEqual(tarinfo.size, 0)
        finally:
            tar.close()
    finally:
        os_helper.rmdir(path)
