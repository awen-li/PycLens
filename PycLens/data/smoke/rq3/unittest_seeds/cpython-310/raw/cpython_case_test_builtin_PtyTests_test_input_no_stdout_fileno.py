# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: PtyTests_test_input_no_stdout_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def child(wpipe):
        print('stdin.isatty():', sys.stdin.isatty(), file=wpipe)
        sys.stdout = io.StringIO()
        input('prompt')
        print('captured:', ascii(sys.stdout.getvalue()), file=wpipe)
    lines = self.run_child(child, b'quux\r')
    expected = ('stdin.isatty(): True', "captured: 'prompt'")
    self.assertSequenceEqual(lines, expected)
