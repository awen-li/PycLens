# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackFormatTests_test_stack_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with captured_output('stderr') as ststderr:
        traceback.print_stack(sys._getframe(1))
    stfile = StringIO()
    traceback.print_stack(sys._getframe(1), file=stfile)
    self.assertEqual(ststderr.getvalue(), stfile.getvalue())
    stfmt = traceback.format_stack(sys._getframe(1))
    self.assertEqual(ststderr.getvalue(), ''.join(stfmt))
