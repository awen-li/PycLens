# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCommandLine_test_sys_xoptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (xoptions, nframe) in (('tracemalloc', 1), ('tracemalloc=1', 1), ('tracemalloc=15', 15)):
        with self.subTest(xoptions=xoptions, nframe=nframe):
            code = 'import tracemalloc; print(tracemalloc.get_traceback_limit())'
            (ok, stdout, stderr) = assert_python_ok('-X', xoptions, '-c', code)
            stdout = stdout.rstrip()
            self.assertEqual(stdout, str(nframe).encode('ascii'))
