# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: PathLikeTests_test_path_commonpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    common_path = self.path.commonpath([self.file_path, self.file_name])
    self.assertPathEqual(common_path, self.file_name)
