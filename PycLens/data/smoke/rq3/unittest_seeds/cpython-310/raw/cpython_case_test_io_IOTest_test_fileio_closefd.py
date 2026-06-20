# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_fileio_closefd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(__file__, 'rb') as f1, self.open(__file__, 'rb') as f2:
        fileio = self.FileIO(f1.fileno(), closefd=False)
        fileio.__init__(f2.fileno(), closefd=False)
        f1.readline()
        fileio.close()
        f2.readline()
