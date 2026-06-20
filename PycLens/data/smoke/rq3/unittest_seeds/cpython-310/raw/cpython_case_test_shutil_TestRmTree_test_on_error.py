# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_on_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.errorState = 0
    os.mkdir(TESTFN)
    self.addCleanup(shutil.rmtree, TESTFN)
    self.child_file_path = os.path.join(TESTFN, 'a')
    self.child_dir_path = os.path.join(TESTFN, 'b')
    os_helper.create_empty_file(self.child_file_path)
    os.mkdir(self.child_dir_path)
    old_dir_mode = os.stat(TESTFN).st_mode
    old_child_file_mode = os.stat(self.child_file_path).st_mode
    old_child_dir_mode = os.stat(self.child_dir_path).st_mode
    new_mode = stat.S_IREAD | stat.S_IEXEC
    os.chmod(self.child_file_path, new_mode)
    os.chmod(self.child_dir_path, new_mode)
    os.chmod(TESTFN, new_mode)
    self.addCleanup(os.chmod, TESTFN, old_dir_mode)
    self.addCleanup(os.chmod, self.child_file_path, old_child_file_mode)
    self.addCleanup(os.chmod, self.child_dir_path, old_child_dir_mode)
    shutil.rmtree(TESTFN, onerror=self.check_args_to_onerror)
    self.assertEqual(self.errorState, 3, 'Expected call to onerror function did not happen.')
