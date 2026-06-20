# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCommandLine_test_verbose_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['nannynag_errored']) as path:
        stdout = textwrap.dedent('offending line: \'\\tprint("world")\\n\'').strip()
        self.validate_cmd('-v', path, stdout=stdout, partial=True)
