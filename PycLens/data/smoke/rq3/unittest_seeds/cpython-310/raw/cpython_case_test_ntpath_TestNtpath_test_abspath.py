# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_abspath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.abspath("C:\\")', 'C:\\')
    with os_helper.temp_cwd(os_helper.TESTFN) as cwd_dir:
        tester('ntpath.abspath("")', cwd_dir)
        tester('ntpath.abspath(" ")', cwd_dir + '\\ ')
        tester('ntpath.abspath("?")', cwd_dir + '\\?')
        (drive, _) = ntpath.splitdrive(cwd_dir)
        tester('ntpath.abspath("/abc/")', drive + '\\abc')
