# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_apropos_empty_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkgdir = os.path.join(TESTFN, 'walkpkg')
    os.mkdir(pkgdir)
    self.addCleanup(rmtree, pkgdir)
    init_path = os.path.join(pkgdir, '__init__.py')
    with open(init_path, 'w') as fobj:
        fobj.write('foo = 1')
    current_mode = stat.S_IMODE(os.stat(pkgdir).st_mode)
    try:
        os.chmod(pkgdir, current_mode & ~stat.S_IEXEC)
        with self.restrict_walk_packages(path=[TESTFN]), captured_stdout() as stdout:
            pydoc.apropos('')
        self.assertIn('walkpkg', stdout.getvalue())
    finally:
        os.chmod(pkgdir, current_mode)
