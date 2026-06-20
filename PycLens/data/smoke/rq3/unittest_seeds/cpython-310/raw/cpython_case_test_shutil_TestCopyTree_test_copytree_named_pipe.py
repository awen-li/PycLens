# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_named_pipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN)
    try:
        subdir = os.path.join(TESTFN, 'subdir')
        os.mkdir(subdir)
        pipe = os.path.join(subdir, 'mypipe')
        try:
            os.mkfifo(pipe)
        except PermissionError as e:
            self.skipTest('os.mkfifo(): %s' % e)
        try:
            shutil.copytree(TESTFN, TESTFN2)
        except shutil.Error as e:
            errors = e.args[0]
            self.assertEqual(len(errors), 1)
            (src, dst, error_msg) = errors[0]
            self.assertEqual('`%s` is a named pipe' % pipe, error_msg)
        else:
            self.fail('shutil.Error should have been raised')
    finally:
        shutil.rmtree(TESTFN, ignore_errors=True)
        shutil.rmtree(TESTFN2, ignore_errors=True)
