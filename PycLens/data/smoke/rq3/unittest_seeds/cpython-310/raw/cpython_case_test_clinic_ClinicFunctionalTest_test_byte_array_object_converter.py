# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_byte_array_object_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.byte_array_object_converter(1)
    byte_arr = bytearray(b'ByteArrayObject')
    self.assertEqual(ac_tester.byte_array_object_converter(byte_arr), (byte_arr,))
