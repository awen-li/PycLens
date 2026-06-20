# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_flush_and_peek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _peek(bufio, n=-1):
        b = bufio.peek(n)
        if n != -1:
            b = b[:n]
        bufio.seek(len(b), 1)
        return b
    self.check_flush_and_read(_peek)
