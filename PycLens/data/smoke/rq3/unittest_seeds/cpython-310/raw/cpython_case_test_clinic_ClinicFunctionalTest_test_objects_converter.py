# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_objects_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.objects_converter()
    self.assertEqual(ac_tester.objects_converter(1, 2), (1, 2))
    self.assertEqual(ac_tester.objects_converter([], 'whatever class'), ([], 'whatever class'))
    self.assertEqual(ac_tester.objects_converter(1), (1, None))
