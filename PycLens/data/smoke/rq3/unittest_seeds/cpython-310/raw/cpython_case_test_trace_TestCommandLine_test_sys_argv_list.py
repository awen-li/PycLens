# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCommandLine_test_sys_argv_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'w', encoding='utf-8') as fd:
        self.addCleanup(unlink, TESTFN)
        fd.write('import sys\n')
        fd.write('print(type(sys.argv))\n')
    (status, direct_stdout, stderr) = assert_python_ok(TESTFN)
    (status, trace_stdout, stderr) = assert_python_ok('-m', 'trace', '-l', TESTFN, PYTHONIOENCODING='utf-8')
    self.assertIn(direct_stdout.strip(), trace_stdout)
