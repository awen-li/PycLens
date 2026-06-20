# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_when_nannynag_error_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['nannynag_errored']) as file_path:
        out = f'{file_path!r}: *** Line 3: trouble in tab city! ***\n'
        out += 'offending line: \'\\tprint("world")\\n\'\n'
        out += 'indent not equal e.g. at tab size 1\n'
        tabnanny.verbose = 1
        self.verify_tabnanny_check(file_path, out=out)
