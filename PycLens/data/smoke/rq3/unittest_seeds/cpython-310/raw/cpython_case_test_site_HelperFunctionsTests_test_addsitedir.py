# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_addsitedir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pth_file = PthFile()
    pth_file.cleanup(prep=True)
    try:
        pth_file.create()
        site.addsitedir(pth_file.base_dir, set())
        self.pth_file_tests(pth_file)
    finally:
        pth_file.cleanup()
