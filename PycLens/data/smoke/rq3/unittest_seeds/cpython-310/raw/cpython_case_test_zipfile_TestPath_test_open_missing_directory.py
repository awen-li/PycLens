# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_open_missing_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zf = zipfile.Path(add_dirs(build_alpharep_fixture()))
    with self.assertRaises(FileNotFoundError):
        zf.joinpath('z').open()
