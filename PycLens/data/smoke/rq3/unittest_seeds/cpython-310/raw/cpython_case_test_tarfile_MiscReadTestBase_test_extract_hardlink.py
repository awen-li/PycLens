# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_extract_hardlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tarname, errorlevel=1, encoding='iso8859-1') as tar:
        tar.extract('ustar/regtype', TEMPDIR, filter='data')
        self.addCleanup(os_helper.unlink, os.path.join(TEMPDIR, 'ustar/regtype'))
        tar.extract('ustar/lnktype', TEMPDIR, filter='data')
        self.addCleanup(os_helper.unlink, os.path.join(TEMPDIR, 'ustar/lnktype'))
        with open(os.path.join(TEMPDIR, 'ustar/lnktype'), 'rb') as f:
            data = f.read()
        self.assertEqual(sha256sum(data), sha256_regtype)
        tar.extract('ustar/symtype', TEMPDIR, filter='data')
        self.addCleanup(os_helper.unlink, os.path.join(TEMPDIR, 'ustar/symtype'))
        with open(os.path.join(TEMPDIR, 'ustar/symtype'), 'rb') as f:
            data = f.read()
        self.assertEqual(sha256sum(data), sha256_regtype)
