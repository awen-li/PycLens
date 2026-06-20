# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_filename_in_syntaxerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_cwd() as cwd:
        file_path = os.path.join(cwd, 't.py')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('f"{a b}"')
        (_, _, stderr) = assert_python_failure(file_path, PYTHONIOENCODING='ascii')
    self.assertIn(file_path.encode('ascii', 'backslashreplace'), stderr)
