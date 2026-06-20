# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_param_default_expression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function("module os\nos.access\n    follow_symlinks: int(c_default='MAXSIZE') = sys.maxsize")
    p = function.parameters['follow_symlinks']
    self.assertEqual(sys.maxsize, p.default)
    self.assertEqual('MAXSIZE', p.converter.c_default)
    s = self.parse_function_should_fail('module os\nos.access\n    follow_symlinks: int = sys.maxsize')
    self.assertEqual(s, "Error on line 0:\nWhen you specify a named constant ('sys.maxsize') as your default value,\nyou MUST specify a valid c_default.\n")
