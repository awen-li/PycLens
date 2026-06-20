# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_flush_and_readinto

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _readinto(bufio, n=-1):
        b = bytearray(n if n >= 0 else 9999)
        n = bufio.readinto(b)
        return bytes(b[:n])
    self.check_flush_and_read(_readinto)
