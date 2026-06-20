# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: Bz2DetectReadTest_test_detect_stream_bz2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(tarname, 'rb') as fobj:
        data = fobj.read()
    with bz2.BZ2File(tmpname, 'wb', compresslevel=1) as fobj:
        fobj.write(data)
    self._testfunc_file(tmpname, 'r|*')
