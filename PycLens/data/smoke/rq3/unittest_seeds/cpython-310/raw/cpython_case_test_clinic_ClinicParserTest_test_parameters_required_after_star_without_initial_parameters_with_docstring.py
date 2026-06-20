# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_parameters_required_after_star_without_initial_parameters_with_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parse_function_should_fail('\nmodule foo\nfoo.bar\n    *\nDocstring here.\n')
