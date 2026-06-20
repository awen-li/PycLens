# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_errored_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as tmp_dir:
        error_file = TemporaryPyFile(SOURCE_CODES['wrong_indented'], directory=tmp_dir)
        code_file = TemporaryPyFile(SOURCE_CODES['error_free'], directory=tmp_dir)
        with error_file as e_file, code_file as c_file:
            err = 'unindent does not match any outer indentation level (<tokenize>, line 3)\n'
            err = f'{e_file!r}: Indentation Error: {err}'
            self.verify_tabnanny_check(tmp_dir, err=err)
