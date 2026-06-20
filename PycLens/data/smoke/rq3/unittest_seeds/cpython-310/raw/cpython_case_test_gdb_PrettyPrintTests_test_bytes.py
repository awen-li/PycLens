# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertGdbRepr(b'')
    self.assertGdbRepr(b'And now for something hopefully the same')
    self.assertGdbRepr(b'string with embedded NUL here \x00 and then some more text')
    self.assertGdbRepr(b'this is a tab:\t this is a slash-N:\n this is a slash-R:\r')
    self.assertGdbRepr(b'this is byte 255:\xff and byte 128:\x80')
    self.assertGdbRepr(bytes([b for b in range(255)]))
