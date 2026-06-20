# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCoverageCommandLineOutput_test_cover_files_written_no_highlight

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracedir = os.path.dirname(os.path.abspath(trace.__file__))
    tracecoverpath = os.path.join(tracedir, 'trace.cover')
    unlink(tracecoverpath)
    argv = '-m trace --count'.split() + [self.codefile]
    (status, stdout, stderr) = assert_python_ok(*argv)
    self.assertEqual(stderr, b'')
    self.assertFalse(os.path.exists(tracecoverpath))
    self.assertTrue(os.path.exists(self.coverfile))
    with open(self.coverfile, encoding='iso-8859-15') as f:
        self.assertEqual(f.read(), "       # coding: iso-8859-15\n    1: x = 'spœm'\n    1: if []:\n           print('unreachable')\n")
