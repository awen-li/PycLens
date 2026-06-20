# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_syntax_error_various_offsets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for offset in range(-5, 10):
        for add in [0, 2]:
            text = ' ' * add + 'text%d' % offset
            expected = ['  File "file.py", line 1']
            if offset < 1:
                expected.append('    %s' % text.lstrip())
            elif offset <= 6:
                expected.append('    %s' % text.lstrip())
                expected.append('    %s^' % (' ' * (offset - 1)))
            else:
                expected.append('    %s' % text.lstrip())
                expected.append('    %s^' % (' ' * 5))
            expected.append('SyntaxError: msg')
            expected.append('')
            err = self.get_report(SyntaxError('msg', ('file.py', 1, offset + add, text)))
            exp = '\n'.join(expected)
            self.assertEqual(exp, err)
