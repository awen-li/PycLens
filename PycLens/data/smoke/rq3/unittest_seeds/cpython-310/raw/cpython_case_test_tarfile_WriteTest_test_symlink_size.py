# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_symlink_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join(TEMPDIR, 'symlink')
    os.symlink('link_target', path)
    try:
        tar = tarfile.open(tmpname, self.mode)
        try:
            tarinfo = tar.gettarinfo(path)
            self.assertEqual(tarinfo.size, 0)
        finally:
            tar.close()
    finally:
        os_helper.unlink(path)
