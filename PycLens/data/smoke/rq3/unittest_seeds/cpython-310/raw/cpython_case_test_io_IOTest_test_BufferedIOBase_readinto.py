# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_BufferedIOBase_readinto

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Reader(self.BufferedIOBase):

        def __init__(self, avail):
            self.avail = avail

        def read(self, size):
            result = self.avail[:size]
            self.avail = self.avail[size:]
            return result

        def read1(self, size):
            """Returns no more than 5 bytes at once"""
            return self.read(min(size, 5))
    tests = (('readinto', 10, 5, 5), ('readinto', 10, 6, 6), ('readinto', 5, 6, 5), ('readinto', 6, 7, 6), ('readinto', 10, 0, 0), ('readinto1', 10, 5, 5), ('readinto1', 10, 6, 5), ('readinto1', 5, 6, 5), ('readinto1', 6, 7, 5), ('readinto1', 10, 0, 0))
    UNUSED_BYTE = 129
    for test in tests:
        with self.subTest(test):
            (method, avail, request, result) = test
            reader = Reader(bytes(range(avail)))
            buffer = bytearray((UNUSED_BYTE,) * request)
            method = getattr(reader, method)
            self.assertEqual(method(buffer), result)
            self.assertEqual(len(buffer), request)
            self.assertSequenceEqual(buffer[:result], range(result))
            unused = (UNUSED_BYTE,) * (request - result)
            self.assertSequenceEqual(buffer[result:], unused)
            self.assertEqual(len(reader.avail), avail - result)
