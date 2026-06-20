# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_symlink_prefix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    self.addCleanup(os_helper.unlink, ABSTFN + '3')
    self.addCleanup(os_helper.unlink, '\\\\?\\' + ABSTFN + '3.')
    self.addCleanup(os_helper.unlink, ABSTFN + '3link')
    self.addCleanup(os_helper.unlink, ABSTFN + '3.link')
    with open(ABSTFN + '3', 'wb') as f:
        f.write(b'0')
    os.symlink(ABSTFN + '3', ABSTFN + '3link')
    with open('\\\\?\\' + ABSTFN + '3.', 'wb') as f:
        f.write(b'1')
    os.symlink('\\\\?\\' + ABSTFN + '3.', ABSTFN + '3.link')
    self.assertPathEqual(ntpath.realpath(ABSTFN + '3link'), ABSTFN + '3')
    self.assertPathEqual(ntpath.realpath(ABSTFN + '3.link'), '\\\\?\\' + ABSTFN + '3.')
    with open(ntpath.realpath(ABSTFN + '3link'), 'rb') as f:
        self.assertEqual(f.read(), b'0')
    with open(ntpath.realpath(ABSTFN + '3.link'), 'rb') as f:
        self.assertEqual(f.read(), b'1')
    self.assertPathEqual(ntpath.realpath('\\\\?\\' + ABSTFN + '3link'), '\\\\?\\' + ABSTFN + '3')
    self.assertPathEqual(ntpath.realpath('\\\\?\\' + ABSTFN + '3.link'), '\\\\?\\' + ABSTFN + '3.')
