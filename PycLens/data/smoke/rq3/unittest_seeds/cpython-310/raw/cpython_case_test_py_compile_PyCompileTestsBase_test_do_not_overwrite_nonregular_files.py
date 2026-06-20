# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_do_not_overwrite_nonregular_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(FileExistsError):
        py_compile.compile(self.source_path, os.devnull)
