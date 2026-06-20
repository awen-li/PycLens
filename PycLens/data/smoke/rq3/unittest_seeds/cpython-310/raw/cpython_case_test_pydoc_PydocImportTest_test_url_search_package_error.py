# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_url_search_package_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkgdir = os.path.join(TESTFN, 'test_error_package')
    os.mkdir(pkgdir)
    init = os.path.join(pkgdir, '__init__.py')
    with open(init, 'wt', encoding='ascii') as f:
        f.write('raise ValueError("ouch")\n')
    with self.restrict_walk_packages(path=[TESTFN]):
        saved_paths = tuple(sys.path)
        sys.path.insert(0, TESTFN)
        try:
            with self.assertRaisesRegex(ValueError, 'ouch'):
                import test_error_package
            text = self.call_url_handler('search?key=test_error_package', 'Pydoc: Search Results')
            found = '<a href="test_error_package.html">test_error_package</a>'
            self.assertIn(found, text)
        finally:
            sys.path[:] = saved_paths
