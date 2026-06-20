# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd.py
# case: TestAlternateInput_test_file_with_missing_final_nl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = io.StringIO('print test\nprint test2')
    output = io.StringIO()
    cmd = self.simplecmd(stdin=input, stdout=output)
    cmd.use_rawinput = False
    cmd.cmdloop()
    self.assertMultiLineEqual(output.getvalue(), '(Cmd) test\n(Cmd) test2\n(Cmd) ')
