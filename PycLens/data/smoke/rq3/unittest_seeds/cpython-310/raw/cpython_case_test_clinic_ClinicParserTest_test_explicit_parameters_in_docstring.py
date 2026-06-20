# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_explicit_parameters_in_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function("\nmodule foo\nfoo.bar\n  x: int\n     Documentation for x.\n  y: int\n\nThis is the documentation for foo.\n\nOkay, we're done here.\n")
    self.assertEqual("\nbar($module, /, x, y)\n--\n\nThis is the documentation for foo.\n\n  x\n    Documentation for x.\n\nOkay, we're done here.\n".strip(), function.docstring)
