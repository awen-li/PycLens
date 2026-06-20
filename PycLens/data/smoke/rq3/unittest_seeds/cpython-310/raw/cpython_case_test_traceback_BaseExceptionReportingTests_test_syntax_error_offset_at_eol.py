# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_syntax_error_offset_at_eol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def e():
        raise SyntaxError('', ('', 0, 5, 'hello'))
    msg = self.get_report(e).splitlines()
    self.assertEqual(msg[-2], '        ^')

    def e():
        exec('x = 5 | 4 |')
    msg = self.get_report(e).splitlines()
    self.assertEqual(msg[-2], '               ^')
