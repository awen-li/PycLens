# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_str_converter_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.str_converter_encoding(1)
    self.assertEqual(ac_tester.str_converter_encoding('a', 'b', 'c'), ('a', 'b', 'c'))
    with self.assertRaises(TypeError):
        ac_tester.str_converter_encoding('a', b'b\x00b', 'c')
    self.assertEqual(ac_tester.str_converter_encoding('a', b'b', bytearray([ord('c')])), ('a', 'b', 'c'))
    self.assertEqual(ac_tester.str_converter_encoding('a', b'b', bytearray([ord('c'), 0, ord('c')])), ('a', 'b', 'c\x00c'))
    self.assertEqual(ac_tester.str_converter_encoding('a', b'b', b'c\x00c'), ('a', 'b', 'c\x00c'))
