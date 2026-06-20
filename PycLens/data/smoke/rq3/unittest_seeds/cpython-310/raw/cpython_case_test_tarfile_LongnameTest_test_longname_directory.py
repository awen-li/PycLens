# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LongnameTest_test_longname_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    longdir = 'a' * 101 + '/'
    with os_helper.temp_cwd():
        with tarfile.open(tmpname, 'w') as tar:
            tar.format = self.format
            try:
                os.mkdir(longdir)
                tar.add(longdir)
            finally:
                os.rmdir(longdir)
        with tarfile.open(tmpname) as tar:
            self.assertIsNotNone(tar.getmember(longdir))
            self.assertIsNotNone(tar.getmember(longdir.removesuffix('/')))
