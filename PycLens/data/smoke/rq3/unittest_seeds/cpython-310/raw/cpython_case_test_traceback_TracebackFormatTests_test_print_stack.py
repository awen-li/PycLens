# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackFormatTests_test_print_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def prn():
        traceback.print_stack()
    with captured_output('stderr') as stderr:
        prn()
    lineno = prn.__code__.co_firstlineno
    self.assertEqual(stderr.getvalue().splitlines()[-4:], ['  File "%s", line %d, in test_print_stack' % (__file__, lineno + 3), '    prn()', '  File "%s", line %d, in prn' % (__file__, lineno + 1), '    traceback.print_stack()'])
