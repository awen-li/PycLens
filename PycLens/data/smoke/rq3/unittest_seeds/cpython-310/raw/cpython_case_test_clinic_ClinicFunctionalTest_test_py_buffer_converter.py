# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_py_buffer_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.py_buffer_converter('a', 'b')
    self.assertEqual(ac_tester.py_buffer_converter('abc', bytearray([1, 2, 3])), (b'abc', b'\x01\x02\x03'))
