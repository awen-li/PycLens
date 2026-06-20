# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_doctest.py
# case: TestDocTestFinder_test_empty_namespace_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkg_name = 'doctest_empty_pkg'
    with tempfile.TemporaryDirectory() as parent_dir:
        pkg_dir = os.path.join(parent_dir, pkg_name)
        os.mkdir(pkg_dir)
        sys.path.append(parent_dir)
        try:
            mod = importlib.import_module(pkg_name)
        finally:
            import_helper.forget(pkg_name)
            sys.path.pop()
        include_empty_finder = doctest.DocTestFinder(exclude_empty=False)
        exclude_empty_finder = doctest.DocTestFinder(exclude_empty=True)
        self.assertEqual(len(include_empty_finder.find(mod)), 1)
        self.assertEqual(len(exclude_empty_finder.find(mod)), 0)
