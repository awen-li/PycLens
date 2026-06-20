# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_init_with_no_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('\nmodule foo\nclass foo.Bar "unused" "notneeded"\nfoo.Bar.__init__\n\nDocstring\n\n', signatures_in_block=3, function_index=2)
    self.assertEqual('Bar()\n--\n\nDocstring', function.docstring)
    self.assertEqual(1, len(function.parameters))
