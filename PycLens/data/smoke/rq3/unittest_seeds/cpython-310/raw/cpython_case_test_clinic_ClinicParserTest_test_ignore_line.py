# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_ignore_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    block = self.parse('#\nmodule os\nos.access')
    (module, function) = block.signatures
    self.assertEqual('access', function.name)
    self.assertEqual('os', module.name)
