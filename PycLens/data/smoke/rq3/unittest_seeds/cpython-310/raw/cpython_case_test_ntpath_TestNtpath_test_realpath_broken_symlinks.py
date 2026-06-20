# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_broken_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    os.mkdir(ABSTFN)
    self.addCleanup(os_helper.rmtree, ABSTFN)
    with os_helper.change_cwd(ABSTFN):
        os.mkdir('subdir')
        os.chdir('subdir')
        os.symlink('.', 'recursive')
        os.symlink('..', 'parent')
        os.chdir('..')
        os.symlink('.', 'self')
        os.symlink('missing', 'broken')
        os.symlink('broken\\bar', 'broken1')
        os.symlink('self\\self\\broken', 'broken2')
        os.symlink('subdir\\parent\\subdir\\parent\\broken', 'broken3')
        os.symlink(ABSTFN + '\\broken', 'broken4')
        os.symlink('recursive\\..\\broken', 'broken5')
        self.assertPathEqual(ntpath.realpath('broken'), ABSTFN + '\\missing')
        self.assertPathEqual(ntpath.realpath('broken\\foo'), ABSTFN + '\\missing\\foo')
        self.assertPathEqual(ntpath.realpath('broken1'), ABSTFN + '\\broken\\bar')
        self.assertPathEqual(ntpath.realpath('broken1\\baz'), ABSTFN + '\\broken\\bar\\baz')
        self.assertPathEqual(ntpath.realpath('broken2'), ABSTFN + '\\self\\self\\missing')
        self.assertPathEqual(ntpath.realpath('broken3'), ABSTFN + '\\subdir\\parent\\subdir\\parent\\missing')
        self.assertPathEqual(ntpath.realpath('broken4'), ABSTFN + '\\missing')
        self.assertPathEqual(ntpath.realpath('broken5'), ABSTFN + '\\missing')
        self.assertPathEqual(ntpath.realpath(b'broken'), os.fsencode(ABSTFN + '\\missing'))
        self.assertPathEqual(ntpath.realpath(b'broken\\foo'), os.fsencode(ABSTFN + '\\missing\\foo'))
        self.assertPathEqual(ntpath.realpath(b'broken1'), os.fsencode(ABSTFN + '\\broken\\bar'))
        self.assertPathEqual(ntpath.realpath(b'broken1\\baz'), os.fsencode(ABSTFN + '\\broken\\bar\\baz'))
        self.assertPathEqual(ntpath.realpath(b'broken2'), os.fsencode(ABSTFN + '\\self\\self\\missing'))
        self.assertPathEqual(ntpath.realpath(b'broken3'), os.fsencode(ABSTFN + '\\subdir\\parent\\subdir\\parent\\missing'))
        self.assertPathEqual(ntpath.realpath(b'broken4'), os.fsencode(ABSTFN + '\\missing'))
        self.assertPathEqual(ntpath.realpath(b'broken5'), os.fsencode(ABSTFN + '\\missing'))
