# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_bool_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.bool_converter(False, False, 'not a int')
    self.assertEqual(ac_tester.bool_converter(), (True, True, True))
    self.assertEqual(ac_tester.bool_converter('', [], 5), (False, False, True))
    self.assertEqual(ac_tester.bool_converter(('not empty',), {1: 2}, 0), (True, True, False))
