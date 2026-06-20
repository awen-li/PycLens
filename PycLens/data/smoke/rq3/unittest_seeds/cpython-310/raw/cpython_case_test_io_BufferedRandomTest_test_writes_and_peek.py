# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_writes_and_peek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _peek(bufio):
        bufio.peek(1)
    self.check_writes(_peek)

    def _peek(bufio):
        pos = bufio.tell()
        bufio.seek(-1, 1)
        bufio.peek(1)
        bufio.seek(pos, 0)
    self.check_writes(_peek)
