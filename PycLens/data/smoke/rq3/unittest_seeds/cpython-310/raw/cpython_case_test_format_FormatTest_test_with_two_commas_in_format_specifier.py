# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_with_two_commas_in_format_specifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    error_msg = re.escape("Cannot specify ',' with ','.")
    with self.assertRaisesRegex(ValueError, error_msg):
        '{:,,}'.format(1)
