# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_param

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('module os\nos.access\n   path: int')
    self.assertEqual('access', function.name)
    self.assertEqual(2, len(function.parameters))
    p = function.parameters['path']
    self.assertEqual('path', p.name)
    self.assertIsInstance(p.converter, clinic.int_converter)
