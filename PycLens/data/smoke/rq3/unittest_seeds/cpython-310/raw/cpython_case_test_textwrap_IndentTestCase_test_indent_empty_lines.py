# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCase_test_indent_empty_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prefix = '  '
    expected = ('Hi.\nThis is a test.\nTesting.', 'Hi.\nThis is a test.\n  \nTesting.', '  \nHi.\nThis is a test.\nTesting.\n', 'Hi.\r\nThis is a test.\r\nTesting.\r\n', '  \nHi.\r\nThis is a test.\n  \r\nTesting.\r\n  \n')
    predicate = lambda line: not line.strip()
    for (text, expect) in zip(self.CASES, expected):
        self.assertEqual(indent(text, prefix, predicate), expect)
