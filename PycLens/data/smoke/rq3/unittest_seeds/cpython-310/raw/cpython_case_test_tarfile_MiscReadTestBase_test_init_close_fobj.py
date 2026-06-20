# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_init_close_fobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    empty = os.path.join(TEMPDIR, 'empty')
    with open(empty, 'wb') as fobj:
        fobj.write(b'')
    try:
        tar = object.__new__(tarfile.TarFile)
        try:
            tar.__init__(empty)
        except tarfile.ReadError:
            self.assertTrue(tar.fileobj.closed)
        else:
            self.fail('ReadError not raised')
    finally:
        os_helper.unlink(empty)
