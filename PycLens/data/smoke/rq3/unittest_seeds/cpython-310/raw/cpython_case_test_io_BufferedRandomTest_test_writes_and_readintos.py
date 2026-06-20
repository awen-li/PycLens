# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_writes_and_readintos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _read(bufio):
        bufio.seek(-1, 1)
        bufio.readinto(bytearray(1))
    self.check_writes(_read)
