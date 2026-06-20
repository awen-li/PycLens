# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: MaxLinesTestCase_test_placeholder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wrap(self.text, 12, ['Hello...'], max_lines=1, placeholder='...')
    self.check_wrap(self.text, 12, ['Hello there,', 'how are...'], max_lines=2, placeholder='...')
    with self.assertRaises(ValueError):
        wrap(self.text, 16, initial_indent='    ', max_lines=1, placeholder=' [truncated]...')
    with self.assertRaises(ValueError):
        wrap(self.text, 16, subsequent_indent='    ', max_lines=2, placeholder=' [truncated]...')
    self.check_wrap(self.text, 16, ['    Hello there,', '  [truncated]...'], max_lines=2, initial_indent='    ', subsequent_indent='  ', placeholder=' [truncated]...')
    self.check_wrap(self.text, 16, ['  [truncated]...'], max_lines=1, initial_indent='  ', subsequent_indent='    ', placeholder=' [truncated]...')
    self.check_wrap(self.text, 80, [self.text], placeholder='.' * 1000)
