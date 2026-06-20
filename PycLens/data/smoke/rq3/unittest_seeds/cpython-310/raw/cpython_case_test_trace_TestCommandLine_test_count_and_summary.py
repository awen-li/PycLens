# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCommandLine_test_count_and_summary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = f'{TESTFN}.py'
    coverfilename = f'{TESTFN}.cover'
    modulename = os.path.basename(TESTFN)
    with open(filename, 'w', encoding='utf-8') as fd:
        self.addCleanup(unlink, filename)
        self.addCleanup(unlink, coverfilename)
        fd.write(textwrap.dedent('                x = 1\n                y = 2\n\n                def f():\n                    return x + y\n\n                for i in range(10):\n                    f()\n            '))
    (status, stdout, _) = assert_python_ok('-m', 'trace', '-cs', filename, PYTHONIOENCODING='utf-8')
    stdout = stdout.decode()
    self.assertEqual(status, 0)
    self.assertIn('lines   cov%   module   (path)', stdout)
    self.assertIn(f'6   100%   {modulename}   ({filename})', stdout)
