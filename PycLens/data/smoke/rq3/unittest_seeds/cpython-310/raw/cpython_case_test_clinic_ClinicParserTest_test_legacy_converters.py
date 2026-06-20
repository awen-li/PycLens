# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_legacy_converters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    block = self.parse('module os\nos.access\n   path: "s"')
    (module, function) = block.signatures
    self.assertIsInstance(function.parameters['path'].converter, clinic.str_converter)
