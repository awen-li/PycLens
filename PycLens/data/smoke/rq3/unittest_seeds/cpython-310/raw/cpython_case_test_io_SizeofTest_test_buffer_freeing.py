# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: SizeofTest_test_buffer_freeing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bufsize = 4096
    rawio = self.MockRawIO()
    bufio = self.tp(rawio, buffer_size=bufsize)
    size = sys.getsizeof(bufio) - bufsize
    bufio.close()
    self.assertEqual(sys.getsizeof(bufio), size)
