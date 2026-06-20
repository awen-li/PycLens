# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_when_wrong_indented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['wrong_indented']) as file_path:
        err = 'unindent does not match any outer indentation level (<tokenize>, line 3)\n'
        err = f'{file_path!r}: Indentation Error: {err}'
        self.verify_tabnanny_check(file_path, err=err)
