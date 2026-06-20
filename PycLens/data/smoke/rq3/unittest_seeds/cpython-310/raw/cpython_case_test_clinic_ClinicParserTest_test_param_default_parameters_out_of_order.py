# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_param_default_parameters_out_of_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.parse_function_should_fail('\nmodule os\nos.access\n    follow_symlinks: bool = True\n    something_else: str')
    self.assertEqual(s, "Error on line 0:\nCan't have a parameter without a default ('something_else')\nafter a parameter with a default!\n")
