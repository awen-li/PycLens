# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_no_pycache_in_non_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data_dir = os.path.join(self.directory, 'data')
    data_file = os.path.join(data_dir, 'file')
    os.mkdir(data_dir)
    with open(data_file, 'wb'):
        pass
    compileall.compile_file(data_file)
    self.assertFalse(os.path.exists(os.path.join(data_dir, '__pycache__')))
