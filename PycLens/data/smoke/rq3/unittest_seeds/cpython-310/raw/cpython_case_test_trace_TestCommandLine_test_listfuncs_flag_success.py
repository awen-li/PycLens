# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCommandLine_test_listfuncs_flag_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = TESTFN + '.py'
    modulename = os.path.basename(TESTFN)
    with open(filename, 'w', encoding='utf-8') as fd:
        self.addCleanup(unlink, filename)
        fd.write('a = 1\n')
        (status, stdout, stderr) = assert_python_ok('-m', 'trace', '-l', filename, PYTHONIOENCODING='utf-8')
        self.assertIn(b'functions called:', stdout)
        expected = f'filename: {filename}, modulename: {modulename}, funcname: <module>'
        self.assertIn(expected.encode(), stdout)
