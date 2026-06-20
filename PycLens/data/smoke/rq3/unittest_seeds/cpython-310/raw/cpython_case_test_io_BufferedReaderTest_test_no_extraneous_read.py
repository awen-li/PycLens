# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_no_extraneous_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bufsize = 16
    for n in (2, bufsize - 1, bufsize, bufsize + 1, bufsize * 2):
        rawio = self.MockRawIO([b'x' * n])
        bufio = self.tp(rawio, bufsize)
        self.assertEqual(bufio.read(n), b'x' * n)
        self.assertEqual(rawio._extraneous_reads, 0, 'failed for {}: {} != 0'.format(n, rawio._extraneous_reads))
        rawio = self.MockRawIO([b'x' * (n - 1), b'x'])
        bufio = self.tp(rawio, bufsize)
        self.assertEqual(bufio.read(n), b'x' * n)
        self.assertEqual(rawio._extraneous_reads, 0, 'failed for {}: {} != 0'.format(n, rawio._extraneous_reads))
