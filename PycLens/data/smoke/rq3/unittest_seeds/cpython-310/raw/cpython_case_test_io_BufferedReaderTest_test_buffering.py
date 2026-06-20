# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_buffering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'abcdefghi'
    dlen = len(data)
    tests = [[100, [3, 1, 4, 8], [dlen, 0]], [100, [3, 3, 3], [dlen]], [4, [1, 2, 4, 2], [4, 4, 1]]]
    for (bufsize, buf_read_sizes, raw_read_sizes) in tests:
        rawio = self.MockFileIO(data)
        bufio = self.tp(rawio, buffer_size=bufsize)
        pos = 0
        for nbytes in buf_read_sizes:
            self.assertEqual(bufio.read(nbytes), data[pos:pos + nbytes])
            pos += nbytes
        self.assertEqual(rawio.read_history, raw_read_sizes)
