# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_buffered_readinto_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Stream(self.BufferedIOBase):

        def read(self, size):
            return b'12345'
        read1 = read
    stream = Stream()
    for method in ('readinto', 'readinto1'):
        with self.subTest(method):
            buffer = byteslike(5)
            self.assertEqual(getattr(stream, method)(buffer), 5)
            self.assertEqual(bytes(buffer), b'12345')
