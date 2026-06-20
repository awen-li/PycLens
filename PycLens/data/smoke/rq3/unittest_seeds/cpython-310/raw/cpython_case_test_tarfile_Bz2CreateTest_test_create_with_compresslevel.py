# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: Bz2CreateTest_test_create_with_compresslevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tmpname, self.mode, compresslevel=1) as tobj:
        tobj.add(self.file_path)
    with tarfile.open(tmpname, 'r:bz2', compresslevel=1) as tobj:
        pass
