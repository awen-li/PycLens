# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCommandLine_test_with_errored_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['wrong_indented']) as file_path:
        stderr = f'{file_path!r}: Indentation Error: '
        stderr += 'unindent does not match any outer indentation level (<tokenize>, line 3)'
        self.validate_cmd(file_path, stderr=stderr)
