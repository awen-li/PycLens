# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_to_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(tests, byteorder, signed=False):
        for (test, expected) in tests.items():
            try:
                self.assertEqual(test.to_bytes(len(expected), byteorder, signed=signed), expected)
            except Exception as err:
                raise AssertionError('failed to convert {0} with byteorder={1} and signed={2}'.format(test, byteorder, signed)) from err
    tests1 = {0: b'\x00', 1: b'\x01', -1: b'\xff', -127: b'\x81', -128: b'\x80', -129: b'\xff\x7f', 127: b'\x7f', 129: b'\x00\x81', -255: b'\xff\x01', -256: b'\xff\x00', 255: b'\x00\xff', 256: b'\x01\x00', 32767: b'\x7f\xff', -32768: b'\xff\x80\x00', 65535: b'\x00\xff\xff', -65536: b'\xff\x00\x00', -8388608: b'\x80\x00\x00'}
    check(tests1, 'big', signed=True)
    tests2 = {0: b'\x00', 1: b'\x01', -1: b'\xff', -127: b'\x81', -128: b'\x80', -129: b'\x7f\xff', 127: b'\x7f', 129: b'\x81\x00', -255: b'\x01\xff', -256: b'\x00\xff', 255: b'\xff\x00', 256: b'\x00\x01', 32767: b'\xff\x7f', -32768: b'\x00\x80', 65535: b'\xff\xff\x00', -65536: b'\x00\x00\xff', -8388608: b'\x00\x00\x80'}
    check(tests2, 'little', signed=True)
    tests3 = {0: b'\x00', 1: b'\x01', 127: b'\x7f', 128: b'\x80', 255: b'\xff', 256: b'\x01\x00', 32767: b'\x7f\xff', 32768: b'\x80\x00', 65535: b'\xff\xff', 65536: b'\x01\x00\x00'}
    check(tests3, 'big', signed=False)
    tests4 = {0: b'\x00', 1: b'\x01', 127: b'\x7f', 128: b'\x80', 255: b'\xff', 256: b'\x00\x01', 32767: b'\xff\x7f', 32768: b'\x00\x80', 65535: b'\xff\xff', 65536: b'\x00\x00\x01'}
    check(tests4, 'little', signed=False)
    self.assertRaises(OverflowError, 256 .to_bytes, 1, 'big', signed=False)
    self.assertRaises(OverflowError, 256 .to_bytes, 1, 'big', signed=True)
    self.assertRaises(OverflowError, 256 .to_bytes, 1, 'little', signed=False)
    self.assertRaises(OverflowError, 256 .to_bytes, 1, 'little', signed=True)
    self.assertRaises(OverflowError, (-1).to_bytes, 2, 'big', signed=False)
    self.assertRaises(OverflowError, (-1).to_bytes, 2, 'little', signed=False)
    self.assertEqual(0 .to_bytes(0, 'big'), b'')
    self.assertEqual(1 .to_bytes(5, 'big'), b'\x00\x00\x00\x00\x01')
    self.assertEqual(0 .to_bytes(5, 'big'), b'\x00\x00\x00\x00\x00')
    self.assertEqual((-1).to_bytes(5, 'big', signed=True), b'\xff\xff\xff\xff\xff')
    self.assertRaises(OverflowError, 1 .to_bytes, 0, 'big')
