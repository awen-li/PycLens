# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCoverageCommandLineOutput_test_cover_files_written_with_highlight

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    argv = '-m trace --count --missing'.split() + [self.codefile]
    (status, stdout, stderr) = assert_python_ok(*argv)
    self.assertTrue(os.path.exists(self.coverfile))
    with open(self.coverfile, encoding='iso-8859-15') as f:
        self.assertEqual(f.read(), textwrap.dedent("                       # coding: iso-8859-15\n                    1: x = 'spœm'\n                    1: if []:\n                >>>>>>     print('unreachable')\n            "))
