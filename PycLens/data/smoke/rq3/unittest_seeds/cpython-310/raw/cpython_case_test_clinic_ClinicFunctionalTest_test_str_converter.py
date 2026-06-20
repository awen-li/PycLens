# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_str_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.str_converter(1)
    with self.assertRaises(TypeError):
        ac_tester.str_converter('a', 'b', 'c')
    with self.assertRaises(ValueError):
        ac_tester.str_converter('a', b'b\x00b', 'c')
    self.assertEqual(ac_tester.str_converter('a', b'b', 'c'), ('a', 'b', 'c'))
    self.assertEqual(ac_tester.str_converter('a', b'b', b'c'), ('a', 'b', 'c'))
    self.assertEqual(ac_tester.str_converter('a', b'b', 'c\x00c'), ('a', 'b', 'c\x00c'))
