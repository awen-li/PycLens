# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_writes_and_read1s

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _read1(bufio):
        bufio.seek(-1, 1)
        bufio.read1(1)
    self.check_writes(_read1)
