# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: SizeofTest_test_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bufsize1 = 4096
    bufsize2 = 8192
    rawio = self.MockRawIO()
    bufio = self.tp(rawio, buffer_size=bufsize1)
    size = sys.getsizeof(bufio) - bufsize1
    rawio = self.MockRawIO()
    bufio = self.tp(rawio, buffer_size=bufsize2)
    self.assertEqual(sys.getsizeof(bufio), size + bufsize2)
