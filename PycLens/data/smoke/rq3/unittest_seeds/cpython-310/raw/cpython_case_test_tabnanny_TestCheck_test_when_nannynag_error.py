# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_when_nannynag_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['nannynag_errored']) as file_path:
        out = f"""{file_path} 3 '\\tprint("world")\\n'\n"""
        self.verify_tabnanny_check(file_path, out=out)
