# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_parser_regression_special_character_in_parameter_column_of_docstring_first_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('\nmodule os\nos.stat\n    path: str\nThis/used to break Clinic!\n')
    self.assertEqual('stat($module, /, path)\n--\n\nThis/used to break Clinic!', function.docstring)
