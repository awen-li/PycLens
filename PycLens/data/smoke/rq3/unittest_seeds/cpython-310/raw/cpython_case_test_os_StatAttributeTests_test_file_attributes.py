# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_file_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = os.stat(self.fname)
    self.check_file_attributes(result)
    self.assertEqual(result.st_file_attributes & stat.FILE_ATTRIBUTE_DIRECTORY, 0)
    dirname = os_helper.TESTFN + 'dir'
    os.mkdir(dirname)
    self.addCleanup(os.rmdir, dirname)
    result = os.stat(dirname)
    self.check_file_attributes(result)
    self.assertEqual(result.st_file_attributes & stat.FILE_ATTRIBUTE_DIRECTORY, stat.FILE_ATTRIBUTE_DIRECTORY)
