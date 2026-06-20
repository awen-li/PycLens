# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_char_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.char_converter(1)
    with self.assertRaises(TypeError):
        ac_tester.char_converter(b'ab')
    chars = [b'A', b'\x07', b'\x08', b'\t', b'\n', b'\x0b', b'\x0c', b'\r', b'"', b"'", b'?', b'\\', b'\x00', b'\xff']
    expected = tuple((ord(c) for c in chars))
    self.assertEqual(ac_tester.char_converter(), expected)
    chars = [b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'0', b'a', b'b', b'c', b'd']
    expected = tuple((ord(c) for c in chars))
    self.assertEqual(ac_tester.char_converter(*chars), expected)
