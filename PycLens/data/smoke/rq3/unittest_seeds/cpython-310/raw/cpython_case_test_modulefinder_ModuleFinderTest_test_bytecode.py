# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_modulefinder.py
# case: ModuleFinderTest_test_bytecode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base_path = os.path.join(TEST_DIR, 'a')
    source_path = base_path + importlib.machinery.SOURCE_SUFFIXES[0]
    bytecode_path = base_path + importlib.machinery.BYTECODE_SUFFIXES[0]
    with open_file(source_path) as file:
        file.write('testing_modulefinder = True\n'.encode('utf-8'))
    py_compile.compile(source_path, cfile=bytecode_path)
    os.remove(source_path)
    self._do_test(bytecode_test)
