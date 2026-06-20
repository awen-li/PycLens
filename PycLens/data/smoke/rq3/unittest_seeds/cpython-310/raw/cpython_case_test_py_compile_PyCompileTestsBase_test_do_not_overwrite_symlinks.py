# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_do_not_overwrite_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink(self.pyc_path + '.actual', self.pyc_path)
    except (NotImplementedError, OSError):
        self.skipTest('need to be able to create a symlink for a file')
    else:
        assert os.path.islink(self.pyc_path)
        with self.assertRaises(FileExistsError):
            py_compile.compile(self.source_path, self.pyc_path)
