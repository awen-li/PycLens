# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_exceptions_propagate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mode = os.stat(self.directory)
    os.chmod(self.directory, stat.S_IREAD)
    try:
        with self.assertRaises(IOError):
            py_compile.compile(self.source_path, self.pyc_path)
    finally:
        os.chmod(self.directory, mode.st_mode)
