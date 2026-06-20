# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: DirectoryTestCase_test_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for item in self.files_to_test():
        if test.support.verbose:
            print(f'Testing {item.absolute()}')
        with self.subTest(filename=item):
            source = read_pyfile(item)
            self.check_ast_roundtrip(source)
