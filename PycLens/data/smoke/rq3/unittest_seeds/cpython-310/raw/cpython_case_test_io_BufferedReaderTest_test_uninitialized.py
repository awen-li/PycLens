# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_uninitialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bufio = self.tp.__new__(self.tp)
    del bufio
    bufio = self.tp.__new__(self.tp)
    self.assertRaisesRegex((ValueError, AttributeError), 'uninitialized|has no attribute', bufio.read, 0)
    bufio.__init__(self.MockRawIO())
    self.assertEqual(bufio.read(0), b'')
