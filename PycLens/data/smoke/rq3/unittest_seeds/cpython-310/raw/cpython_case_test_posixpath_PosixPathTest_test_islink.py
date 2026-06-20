# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_islink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(posixpath.islink(os_helper.TESTFN + '1'), False)
    self.assertIs(posixpath.lexists(os_helper.TESTFN + '2'), False)
    with open(os_helper.TESTFN + '1', 'wb') as f:
        f.write(b'foo')
    self.assertIs(posixpath.islink(os_helper.TESTFN + '1'), False)
    if os_helper.can_symlink():
        os.symlink(os_helper.TESTFN + '1', os_helper.TESTFN + '2')
        self.assertIs(posixpath.islink(os_helper.TESTFN + '2'), True)
        os.remove(os_helper.TESTFN + '1')
        self.assertIs(posixpath.islink(os_helper.TESTFN + '2'), True)
        self.assertIs(posixpath.exists(os_helper.TESTFN + '2'), False)
        self.assertIs(posixpath.lexists(os_helper.TESTFN + '2'), True)
    self.assertIs(posixpath.islink(os_helper.TESTFN + '\udfff'), False)
    self.assertIs(posixpath.islink(os.fsencode(os_helper.TESTFN) + b'\xff'), False)
    self.assertIs(posixpath.islink(os_helper.TESTFN + '\x00'), False)
    self.assertIs(posixpath.islink(os.fsencode(os_helper.TESTFN) + b'\x00'), False)
