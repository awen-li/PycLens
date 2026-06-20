# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCommandLine_test_quiet_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['nannynag_errored']) as file_path:
        stdout = f'{file_path}\n'
        self.validate_cmd('-q', file_path, stdout=stdout)
