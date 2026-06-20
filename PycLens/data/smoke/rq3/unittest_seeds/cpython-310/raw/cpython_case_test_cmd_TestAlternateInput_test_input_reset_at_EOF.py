# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd.py
# case: TestAlternateInput_test_input_reset_at_EOF

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = io.StringIO('print test\nprint test2')
    output = io.StringIO()
    cmd = self.simplecmd2(stdin=input, stdout=output)
    cmd.use_rawinput = False
    cmd.cmdloop()
    self.assertMultiLineEqual(output.getvalue(), '(Cmd) test\n(Cmd) test2\n(Cmd) *** Unknown syntax: EOF\n')
    input = io.StringIO('print \n\n')
    output = io.StringIO()
    cmd.stdin = input
    cmd.stdout = output
    cmd.cmdloop()
    self.assertMultiLineEqual(output.getvalue(), '(Cmd) \n(Cmd) \n(Cmd) *** Unknown syntax: EOF\n')
