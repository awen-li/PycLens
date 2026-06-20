# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_file_utf_8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    extra = "z = 'ሴ'; assert ord(z) == 0x1234\n"
    self.check_encoding('utf-8', extra)
