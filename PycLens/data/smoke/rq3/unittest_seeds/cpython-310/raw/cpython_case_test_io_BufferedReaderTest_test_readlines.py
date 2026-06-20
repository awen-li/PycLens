# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def bufio():
        rawio = self.MockRawIO((b'abc\n', b'd\n', b'ef'))
        return self.tp(rawio)
    self.assertEqual(bufio().readlines(), [b'abc\n', b'd\n', b'ef'])
    self.assertEqual(bufio().readlines(5), [b'abc\n', b'd\n'])
    self.assertEqual(bufio().readlines(None), [b'abc\n', b'd\n', b'ef'])
