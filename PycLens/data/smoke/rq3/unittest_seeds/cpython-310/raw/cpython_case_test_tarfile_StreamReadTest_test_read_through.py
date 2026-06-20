# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: StreamReadTest_test_read_through

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tarinfo in self.tar:
        if not tarinfo.isreg():
            continue
        with self.tar.extractfile(tarinfo) as fobj:
            while True:
                try:
                    buf = fobj.read(512)
                except tarfile.StreamError:
                    self.fail('simple read-through using TarFile.extractfile() failed')
                if not buf:
                    break
