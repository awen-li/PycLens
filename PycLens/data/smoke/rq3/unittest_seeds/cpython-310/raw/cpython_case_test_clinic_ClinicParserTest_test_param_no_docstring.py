# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_param_no_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function("\nmodule os\nos.access\n    follow_symlinks: bool = True\n    something_else: str = ''")
    p = function.parameters['follow_symlinks']
    self.assertEqual(3, len(function.parameters))
    self.assertIsInstance(function.parameters['something_else'].converter, clinic.str_converter)
