# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: StreamWriteTest_test_file_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.path.exists(tmpname):
        os_helper.unlink(tmpname)
    original_umask = os.umask(18)
    try:
        tar = tarfile.open(tmpname, self.mode)
        tar.close()
        mode = os.stat(tmpname).st_mode & 511
        self.assertEqual(mode, 420, 'wrong file permissions')
    finally:
        os.umask(original_umask)
