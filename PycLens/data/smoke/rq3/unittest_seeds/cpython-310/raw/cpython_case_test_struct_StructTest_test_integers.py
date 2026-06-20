# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_integers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import binascii

    class IntTester(unittest.TestCase):

        def __init__(self, format):
            super(IntTester, self).__init__(methodName='test_one')
            self.format = format
            self.code = format[-1]
            self.byteorder = format[:-1]
            if not self.byteorder in byteorders:
                raise ValueError('unrecognized packing byteorder: %s' % self.byteorder)
            self.bytesize = struct.calcsize(format)
            self.bitsize = self.bytesize * 8
            if self.code in tuple('bhilqn'):
                self.signed = True
                self.min_value = -2 ** (self.bitsize - 1)
                self.max_value = 2 ** (self.bitsize - 1) - 1
            elif self.code in tuple('BHILQN'):
                self.signed = False
                self.min_value = 0
                self.max_value = 2 ** self.bitsize - 1
            else:
                raise ValueError('unrecognized format code: %s' % self.code)

        def test_one(self, x, pack=struct.pack, unpack=struct.unpack, unhexlify=binascii.unhexlify):
            format = self.format
            if self.min_value <= x <= self.max_value:
                expected = x
                if self.signed and x < 0:
                    expected += 1 << self.bitsize
                self.assertGreaterEqual(expected, 0)
                expected = '%x' % expected
                if len(expected) & 1:
                    expected = '0' + expected
                expected = expected.encode('ascii')
                expected = unhexlify(expected)
                expected = b'\x00' * (self.bytesize - len(expected)) + expected
                if self.byteorder == '<' or (self.byteorder in ('', '@', '=') and (not ISBIGENDIAN)):
                    expected = string_reverse(expected)
                self.assertEqual(len(expected), self.bytesize)
                got = pack(format, x)
                self.assertEqual(got, expected)
                retrieved = unpack(format, got)[0]
                self.assertEqual(x, retrieved)
                self.assertRaises((struct.error, TypeError), unpack, format, b'\x01' + got)
            else:
                self.assertRaises((OverflowError, ValueError, struct.error), pack, format, x)

        def run(self):
            from random import randrange
            values = []
            for exp in range(self.bitsize + 3):
                values.append(1 << exp)
            for i in range(self.bitsize):
                val = 0
                for j in range(self.bytesize):
                    val = val << 8 | randrange(256)
                values.append(val)
            values.extend([300, 700000, sys.maxsize * 4])
            for base in values:
                for val in (-base, base):
                    for incr in (-1, 0, 1):
                        x = val + incr
                        self.test_one(x)

            class NotAnInt:

                def __int__(self):
                    return 42

            class Indexable(object):

                def __init__(self, value):
                    self._value = value

                def __index__(self):
                    return self._value

            class BadIndex(object):

                def __index__(self):
                    raise TypeError

                def __int__(self):
                    return 42
            self.assertRaises((TypeError, struct.error), struct.pack, self.format, 'a string')
            self.assertRaises((TypeError, struct.error), struct.pack, self.format, randrange)
            self.assertRaises((TypeError, struct.error), struct.pack, self.format, 3 + 42j)
            self.assertRaises((TypeError, struct.error), struct.pack, self.format, NotAnInt())
            self.assertRaises((TypeError, struct.error), struct.pack, self.format, BadIndex())
            for obj in (Indexable(0), Indexable(10), Indexable(17), Indexable(42), Indexable(100), Indexable(127)):
                try:
                    struct.pack(format, obj)
                except:
                    self.fail("integer code pack failed on object with '__index__' method")
            for obj in (Indexable(b'a'), Indexable('b'), Indexable(None), Indexable({'a': 1}), Indexable([1, 2, 3])):
                self.assertRaises((TypeError, struct.error), struct.pack, self.format, obj)
    for (code, byteorder) in iter_integer_formats():
        format = byteorder + code
        t = IntTester(format)
        t.run()
