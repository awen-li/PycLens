# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_py_complex_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.py_complex_converter([])
    self.assertEqual(ac_tester.py_complex_converter(complex(1, 2)), (complex(1, 2),))
    self.assertEqual(ac_tester.py_complex_converter(complex('-1-2j')), (complex('-1-2j'),))
    self.assertEqual(ac_tester.py_complex_converter(-0.5), (-0.5,))
    self.assertEqual(ac_tester.py_complex_converter(10), (10,))
