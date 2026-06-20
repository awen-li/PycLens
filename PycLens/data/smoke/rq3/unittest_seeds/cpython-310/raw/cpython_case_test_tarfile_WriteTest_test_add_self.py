# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_add_self

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dstname = os.path.abspath(tmpname)
    tar = tarfile.open(tmpname, self.mode)
    try:
        self.assertEqual(tar.name, dstname, 'archive name must be absolute')
        tar.add(dstname)
        self.assertEqual(tar.getnames(), [], 'added the archive to itself')
        with os_helper.change_cwd(TEMPDIR):
            tar.add(dstname)
        self.assertEqual(tar.getnames(), [], 'added the archive to itself')
    finally:
        tar.close()
