# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_from_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(tests, byteorder, signed=False):
        for (test, expected) in tests.items():
            try:
                self.assertEqual(int.from_bytes(test, byteorder, signed=signed), expected)
            except Exception as err:
                raise AssertionError('failed to convert {0} with byteorder={1!r} and signed={2}'.format(test, byteorder, signed)) from err
    tests1 = {b'': 0, b'\x00': 0, b'\x00\x00': 0, b'\x01': 1, b'\x00\x01': 1, b'\xff': -1, b'\xff\xff': -1, b'\x81': -127, b'\x80': -128, b'\xff\x7f': -129, b'\x7f': 127, b'\x00\x81': 129, b'\xff\x01': -255, b'\xff\x00': -256, b'\x00\xff': 255, b'\x01\x00': 256, b'\x7f\xff': 32767, b'\x80\x00': -32768, b'\x00\xff\xff': 65535, b'\xff\x00\x00': -65536, b'\x80\x00\x00': -8388608}
    check(tests1, 'big', signed=True)
    tests2 = {b'': 0, b'\x00': 0, b'\x00\x00': 0, b'\x01': 1, b'\x00\x01': 256, b'\xff': -1, b'\xff\xff': -1, b'\x81': -127, b'\x80': -128, b'\x7f\xff': -129, b'\x7f': 127, b'\x81\x00': 129, b'\x01\xff': -255, b'\x00\xff': -256, b'\xff\x00': 255, b'\x00\x01': 256, b'\xff\x7f': 32767, b'\x00\x80': -32768, b'\xff\xff\x00': 65535, b'\x00\x00\xff': -65536, b'\x00\x00\x80': -8388608}
    check(tests2, 'little', signed=True)
    tests3 = {b'': 0, b'\x00': 0, b'\x01': 1, b'\x7f': 127, b'\x80': 128, b'\xff': 255, b'\x01\x00': 256, b'\x7f\xff': 32767, b'\x80\x00': 32768, b'\xff\xff': 65535, b'\x01\x00\x00': 65536}
    check(tests3, 'big', signed=False)
    tests4 = {b'': 0, b'\x00': 0, b'\x01': 1, b'\x7f': 127, b'\x80': 128, b'\xff': 255, b'\x00\x01': 256, b'\xff\x7f': 32767, b'\x00\x80': 32768, b'\xff\xff': 65535, b'\x00\x00\x01': 65536}
    check(tests4, 'little', signed=False)

    class myint(int):
        pass
    self.assertIs(type(myint.from_bytes(b'\x00', 'big')), myint)
    self.assertEqual(myint.from_bytes(b'\x01', 'big'), 1)
    self.assertIs(type(myint.from_bytes(b'\x00', 'big', signed=False)), myint)
    self.assertEqual(myint.from_bytes(b'\x01', 'big', signed=False), 1)
    self.assertIs(type(myint.from_bytes(b'\x00', 'little')), myint)
    self.assertEqual(myint.from_bytes(b'\x01', 'little'), 1)
    self.assertIs(type(myint.from_bytes(b'\x00', 'little', signed=False)), myint)
    self.assertEqual(myint.from_bytes(b'\x01', 'little', signed=False), 1)
    self.assertEqual(int.from_bytes([255, 0, 0], 'big', signed=True), -65536)
    self.assertEqual(int.from_bytes((255, 0, 0), 'big', signed=True), -65536)
    self.assertEqual(int.from_bytes(bytearray(b'\xff\x00\x00'), 'big', signed=True), -65536)
    self.assertEqual(int.from_bytes(bytearray(b'\xff\x00\x00'), 'big', signed=True), -65536)
    self.assertEqual(int.from_bytes(array.array('B', b'\xff\x00\x00'), 'big', signed=True), -65536)
    self.assertEqual(int.from_bytes(memoryview(b'\xff\x00\x00'), 'big', signed=True), -65536)
    self.assertRaises(ValueError, int.from_bytes, [256], 'big')
    self.assertRaises(ValueError, int.from_bytes, [0], 'big\x00')
    self.assertRaises(ValueError, int.from_bytes, [0], 'little\x00')
    self.assertRaises(TypeError, int.from_bytes, '', 'big')
    self.assertRaises(TypeError, int.from_bytes, '\x00', 'big')
    self.assertRaises(TypeError, int.from_bytes, 0, 'big')
    self.assertRaises(TypeError, int.from_bytes, 0, 'big', True)
    self.assertRaises(TypeError, myint.from_bytes, '', 'big')
    self.assertRaises(TypeError, myint.from_bytes, '\x00', 'big')
    self.assertRaises(TypeError, myint.from_bytes, 0, 'big')
    self.assertRaises(TypeError, int.from_bytes, 0, 'big', True)

    class myint2(int):

        def __new__(cls, value):
            return int.__new__(cls, value + 1)
    i = myint2.from_bytes(b'\x01', 'big')
    self.assertIs(type(i), myint2)
    self.assertEqual(i, 2)

    class myint3(int):

        def __init__(self, value):
            self.foo = 'bar'
    i = myint3.from_bytes(b'\x01', 'big')
    self.assertIs(type(i), myint3)
    self.assertEqual(i, 1)
    self.assertEqual(getattr(i, 'foo', 'none'), 'bar')

    class ValidBytes:

        def __bytes__(self):
            return b'\x01'

    class InvalidBytes:

        def __bytes__(self):
            return 'abc'

    class MissingBytes:
        ...

    class RaisingBytes:

        def __bytes__(self):
            1 / 0
    for byte_order in ('big', 'little'):
        self.assertEqual(int.from_bytes(ValidBytes(), byte_order), 1)
        self.assertRaises(TypeError, int.from_bytes, InvalidBytes(), byte_order)
        self.assertRaises(TypeError, int.from_bytes, MissingBytes(), byte_order)
        self.assertRaises(ZeroDivisionError, int.from_bytes, RaisingBytes(), byte_order)
