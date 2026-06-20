# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_pathlike_construction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipfile_ondisk = self.zipfile_ondisk(alpharep)
    pathlike = pathlib.Path(str(zipfile_ondisk))
    zipfile.Path(pathlike)
