# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_when_tokenize_tokenerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['incomplete_expression']) as file_path:
        err = "('EOF in multi-line statement', (7, 0))\n"
        err = f'{file_path!r}: Token Error: {err}'
        self.verify_tabnanny_check(file_path, err=err)
