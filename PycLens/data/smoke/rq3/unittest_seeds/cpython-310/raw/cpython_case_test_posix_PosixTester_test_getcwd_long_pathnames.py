# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_getcwd_long_pathnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirname = 'getcwd-test-directory-0123456789abcdef-01234567890abcdef'
    curdir = os.getcwd()
    base_path = os.path.abspath(os_helper.TESTFN) + '.getcwd'
    try:
        os.mkdir(base_path)
        os.chdir(base_path)
    except:
        return

        def _create_and_do_getcwd(dirname, current_path_length=0):
            try:
                os.mkdir(dirname)
            except:
                raise unittest.SkipTest('mkdir cannot create directory sufficiently deep for getcwd test')
            os.chdir(dirname)
            try:
                os.getcwd()
                if current_path_length < 1027:
                    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
            finally:
                os.chdir('..')
                os.rmdir(dirname)
        _create_and_do_getcwd(dirname)
    finally:
        os.chdir(curdir)
        os_helper.rmtree(base_path)
