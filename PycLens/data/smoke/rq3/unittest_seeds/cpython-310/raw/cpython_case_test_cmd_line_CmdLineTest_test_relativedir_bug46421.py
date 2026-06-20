# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_relativedir_bug46421

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    defaultwd = os.getcwd()
    projectlibpath = os.path.dirname(__file__).removesuffix('test')
    with os_helper.change_cwd(projectlibpath):
        assert_python_ok('-m', 'unittest', 'test/test_longexp.py')
        assert_python_ok('-m', 'unittest', './test/test_longexp.py')
