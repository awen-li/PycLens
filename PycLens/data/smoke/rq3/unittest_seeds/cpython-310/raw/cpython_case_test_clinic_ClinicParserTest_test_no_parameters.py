# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_no_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('\nmodule foo\nfoo.bar\n\nDocstring\n\n')
    self.assertEqual('bar($module, /)\n--\n\nDocstring', function.docstring)
    self.assertEqual(1, len(function.parameters))
