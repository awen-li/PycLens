# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('module window\nwindow.border\n [\n ls : int\n ]\n /\n')
    p = function.parameters['ls']
    self.assertEqual(1, p.group)
