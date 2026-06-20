# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackFormatTests_test_format_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fmt():
        return traceback.format_stack()
    result = fmt()
    lineno = fmt.__code__.co_firstlineno
    self.assertEqual(result[-2:], ['  File "%s", line %d, in test_format_stack\n    result = fmt()\n' % (__file__, lineno + 2), '  File "%s", line %d, in fmt\n    return traceback.format_stack()\n' % (__file__, lineno + 1)])
