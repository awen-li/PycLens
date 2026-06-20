# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_writes_and_seeks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _seekabs(bufio):
        pos = bufio.tell()
        bufio.seek(pos + 1, 0)
        bufio.seek(pos - 1, 0)
        bufio.seek(pos, 0)
    self.check_writes(_seekabs)

    def _seekrel(bufio):
        pos = bufio.seek(0, 1)
        bufio.seek(+1, 1)
        bufio.seek(-1, 1)
        bufio.seek(pos, 0)
    self.check_writes(_seekrel)
